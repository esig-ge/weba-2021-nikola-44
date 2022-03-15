from django.shortcuts import render, redirect
from compte.models import Client

def accueil(request):
    # if request.user.is_authenticated:
    #     print(request.user.username)
    #     r = Client.objects.raw("select * from compte_client inner join auth_user on "
    #                            "('auth_user'.'id' = 'compte_client'.'user_id') where user_id =" + "'"
    #                            + request.user.username + "'")[0]
    #     print(r)
    #     s = Client.objects.get(user__username = request.user.username)
    #     return render(request, 'accueil.html', {'r': s})
    # else:
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
