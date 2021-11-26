# Châtelain Dorian
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CreerUtilisateur, ProfileForm, CommentaireForm, ProfileModifierForm
from django.contrib import messages
from .models import Client
from django.contrib.auth.models import User


def inscriptionPage(request):
    form = CreerUtilisateur()
    profile_form = ProfileForm()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte Créer avec succès, Bienvenue ' + user)
            return redirect('acces')
    context = {'form': form,
               'profile': profile_form,
               }
    return render(request, 'inscription.html', context)


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "Utilisateur ou mot de passe invalide")

    return render(request, 'acces.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accueil')


def gererClient(request):
    clients = Client.objects.all()
    return render(request, '../templates/gererClients.html', {'clients': clients})


def supprimer_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/compte/gererClients')
    context = {'item': client}
    return render(request, '../templates/supprimer_client.html', context)


# partie admin
def modifier_client(request, pk):
    pi = Client.objects.get(id=pk)
    commentaire = CommentaireForm(instance=pi)
    if request.method == 'POST':
        commentaire = CommentaireForm(request.POST, instance=pi)
        if commentaire.is_valid():
            commentaire.save()
            return redirect('/compte/gererClients')
    return render(request, '../templates/modifier_client.html', {'commentaire': commentaire})


# partie client
def profile(request):
    if request.method == 'POST':
        form = ProfileModifierForm(request.POST, instance=request.user.client)
        print(request.user.client)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = ProfileModifierForm(instance=request.user.client)
    context = {
        'form': form,
    }
    return render(request, '../templates/profile.html', context)
