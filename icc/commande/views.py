from django.shortcuts import render, redirect
from .models import Commande
from .forms import CommandeForm


# Create your views here.

def gererCommande(request):
    commande = Commande.objects.all()
    return render(request, '../templates/gererCommande.html', {'commande': commande})


def modifier_commande(request, pk):
    if request.method == 'POST':
        pi = Commande.objects.get(id=pk)
        fm = CommandeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/commande/gererCommande')
    else:
        pi = Commande.objects.get(id=pk)
        fm = CommandeForm(instance=pi)
    return render(request, '../templates/modifier_commande.html', {'form': fm})


def supprimer_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/commande/gererCommande')
    context = {'item': commande}
    return render(request, '../templates/supprimer_commande.html', context)
