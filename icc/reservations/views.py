# FERREIRA STOJKOVIC Nikola
import datetime
import json
import operator
from datetime import timedelta

from django.contrib.admin.views.decorators import staff_member_required
from django.db import connection
from django.db.models import Case, When
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import Reservation, Prestation, ResPres
from compte.models import Client
from .forms import PrestationForm, ReservationForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


# tdd

@staff_member_required
def prestations_tdd(request):
    dico = {}
    for r in ResPres.objects.all():
        if r.prestation.id in dico.keys():
            dico[r.prestation.id] = dico.get(r.prestation.id) + 1
        else:
            dico[r.prestation.id] = 1

    print(dico)
    dico_trie = dict(sorted(dico.items(), key=operator.itemgetter(1), reverse=True))
    print(dico_trie)

    ordre = []
    for cle in dico_trie.keys():
        ordre.append(cle)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ordre)])
    prestation = Prestation.objects.filter(pk__in=ordre).order_by(preserved)

    # prestation = Prestation.objects.all().order_by(dico_trie.keys())
    return render(request, 'reservations/admin/prestations-tdd.html', {'prestations': prestation})
    # return HttpResponse("Classement des prestations")

# PLANNING


def planning(request):
    # prestations = Prestation.objects.all()
    # ty = Prestation.LONGEUR_CHEVEUX
    #
    # types = []
    # for t in ty:
    #     (_, valeur) = t
    #     types.append(valeur)
    #
    # r_jour = Reservation.objects.all().filter(date_heure__date=datetime.date.today()).order_by('date_heure')
    # r_matin = r_jour.exclude(date_heure__time__gt='12:00:00')
    # print(r_matin)
    # for reservation in r_matin:
    #     print(reservation)
    # r_apresmidi = r_jour.exclude(date_heure__time__lt='12:00:00')
    #
    # return render(request, 'reservations/planning.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'types': types, 'prestations': prestations})
    reservations = Reservation.objects.all().order_by('-date').order_by('-heure')
    return render(request, 'reservations/mes-reservations.html', {'reservations': reservations})


# @app.route('/reservations/<string:jour>', methods=['GET'])
def test(request):  # ajouter un paramètre jour
    prestations = Prestation.objects.all()
    ty = Prestation.LONGEUR_CHEVEUX

    types = []
    for t in ty:
        (_, valeur) = t
        types.append(valeur)
    print('Voici les types de cheveux: ' + str(type(types)), types)
    r_jour = Reservation.objects.all().filter(date=datetime.date.today()).order_by('date').order_by('heure')
    print(type(r_jour))
    # r_jour.filter(heure=datetime.date.today()).order_by('heure')
    r_matin = r_jour.exclude(heure__gt='12:00:00')
    r_apresmidi = r_jour.exclude(heure__lt='12:00:00')

    print(r_matin)
    print(r_apresmidi)
    print(r_jour)
    for i in r_jour:
        print(i.date)
    return render(request, 'reservations/test.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'prestations': prestations, 'types': types})


def ajax(request, d, m, y):
    print('Vous avez appellez Ajax!!')
    print(datetime.datetime(y, m, d))
    r_jour = Reservation.objects.all().filter(date=datetime.datetime(y, m, d)).order_by('date').order_by('heure')
    r_matin = r_jour.exclude(heure__gt='12:00:00')
    r_apresmidi = r_jour.exclude(heure__lt='12:00:00')
    qs_json_matin = serializers.serialize('json', r_matin)
    qs_json_apresmidi = serializers.serialize('json', r_apresmidi)
    qs_json_list = [*r_matin, *r_apresmidi]
    data_json = serializers.serialize('json', qs_json_list)
    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(data_json, content_type='application/json')
    # return render(request, 'reservations/test.html', {'r_matin': qs_json_matin, 'r_apresmidi': qs_json_apresmidi})


def test_prestations(request):
    prestations = Prestation.objects.all()

    noms = []
    for prestation in prestations:
        if prestation.pour != '/':
            if prestation.nom in noms:
                pass
            else:
                noms.append(prestation.nom)
    # print(noms)

    prix = []

    for nom in noms:
        objects = Prestation.objects.all().filter(nom=nom)
        p = []
        for o in objects:
            p.append(o.prix)
        tup = tuple(p)
        # print(nom)
        # print(tup)
        # print(nom + ' - ' + tup.__str__())
        prix.append(tup)
    # print(prix)

    dico = {}
    cpt = 0
    for nom in noms:
        dico[noms[cpt]] = (prix[cpt])
        cpt += 1
    print(dico)

    return render(request, 'reservations/test-prestations.html', {'prestations': prestations, 'dico': dico})


# ESPACE ADMIN


# RESERVATIONS


def ajouter_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        print('print', request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.client = Client.objects.get(user=request.user)
            temp.save()
            print('Temp : ', temp)
            prestations = request.POST.getlist('prestations')
            for prestation in prestations:
                ResPres.objects.create(reservation=temp, prestation=Prestation.objects.get(id=prestation))
            return redirect('mes-reservations')
    return render(request, 'reservations/formulaire/reservation/ajouter-reservation.html', {'form': form})


def supprimer_reservation(request, id):
    reservation = Reservation.objects.get(id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('mes-reservations')
    return render(request, 'reservations/formulaire/reservation/supprimer-reservation.html', {'reservation': reservation})


def mes_reservations(request):
    res_pres = ResPres.objects.all()
    reservations = Reservation.objects.all().filter(client__user=request.user).order_by('-date')
    total = {}
    for reservation in reservations:
        calcul = 0
        for prestation in reservation.prestations.all():
            calcul += prestation.prix
        total[reservation.id] = calcul
    return render(request, 'reservations/mes-reservations.html', {'reservations': reservations, 'total': total, 'res_pres': res_pres})


def reservations(request):
    res_pres = ResPres.objects.all()
    reservations = Reservation.objects.all().filter(client__user=request.user).order_by('date')
    total = {}
    for reservation in reservations:
        calcul = 0
        for prestation in reservation.prestations.all():
            calcul += prestation.prix
        total[reservation.id] = calcul
    return render(request, 'reservations/reservations.html', {'reservations': reservations, 'total': total, 'res_pres': res_pres})


# PRESTATIONS


def prestations_admin(request):
    prestation = Prestation.objects.all().order_by('nom', 'pour')
    return render(request, 'reservations/admin/prestations.html', {'prestations': prestation})


def ajouter_prestation(request):
    form = PrestationForm()
    if request.method == 'POST':
        form = PrestationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/ajouter-prestation.html', {'form': form})


def modifier_prestation(request, id):
    prestation = Prestation.objects.get(id=id)
    form = PrestationForm(instance=prestation)
    if request.method == 'POST':
        form = PrestationForm(request.POST, instance=prestation)
        if form.is_valid():
            form.save()
            return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/modifier-prestation.html', {'form': form})


def supprimer_prestation(request, id):
    prestation = Prestation.objects.get(id=id)
    if request.method == 'POST':
        prestation.delete()
        return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/supprimer-prestation.html', {'prestation': prestation})


def prestations(request):
    return render(request, 'reservations/prestations.html')
