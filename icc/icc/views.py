from django.shortcuts import render, redirect


def accueil(request):
    return render(request, 'accueil.html')


def produits(request):
    return render(request, 'produits.html')


def acces(request):
    return render(request, 'acces.html')


def accueilAdmin(request):
    return render(request, 'accueilAdmin.html')


def gererProduits(request):
    return render(request, 'gererProduit.html')


def gererClients(request):
    return render(request, 'gererClients.html')


def gererSalon(request):
    return render(request, 'gererSalon.html')
