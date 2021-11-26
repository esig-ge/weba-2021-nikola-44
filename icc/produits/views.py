# Zumeri Faton et Châtelain Dorian
import stripe
from django.shortcuts import render, redirect
from .forms import ProduitForm
from .models import Produit
from django.views import View
from commande.models import *
from django.http import JsonResponse
import json


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(client=client, complete=False)
        items = commande.commandeitem_set.all()
        cartItems = commande.get_cart_items
    else:
        items = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = commande['get_cart_items']

    produits = Produit.objects.all()
    print(produits)
    context = {'produits': produits, 'cartItems': cartItems, 'categorie': Produit.Categorie_prod}
    return render(request, 'produits.html', context)


def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(client=client, complete=False)
        items = commande.commandeitem_set.all()
        cartItems = commande.get_cart_items
    else:
        items = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = commande['get_cart_items']

    context = {'items': items, 'commande': commande, 'cartItems': cartItems}
    # print(items)
    # print(client)
    # print(commande)
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(client=client, complete=False)
        items = commande.commandeitem_set.all()
        cartItems = commande.get_cart_items
    else:
        items = []
        commande = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = commande['get_cart_items']

    context = {'items': items, 'commande': commande, 'cartItems': cartItems}
    # context = {}
    if request.method == 'POST':
        return redirect('../landing.html', id=2)
    return render(request, 'checkout.html', context)


def gererProduit(request):
    produits = Produit.objects.all()
    return render(request, '../templates/gererProduit.html', {'produits': produits})


def ajouter_produit(request):
    if request.method == "POST":
        fm = ProduitForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('/produits/gererProduits')
    else:
        fm = ProduitForm()
    return render(request, '../templates/ajouter_produit.html', {'form': fm})


def modifier_produit(request, pk):
    if request.method == 'POST':
        pi = Produit.objects.get(id=pk)
        fm = ProduitForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/produits/gererProduits')
    else:
        pi = Produit.objects.get(id=pk)
        fm = ProduitForm(instance=pi)
    return render(request, '../templates/modifier_produit.html', {'form': fm})


def supprimer_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/produits/gererProduits')
    context = {'item': produit}
    return render(request, '../templates/supprimer_produit.html', context)


def updateItem(request):
    data = json.loads(request.body)
    produitId = data['produitId']
    action = data['action']

    print('Action:', action)
    print('produitId:', produitId)

    client = request.user.client
    produit = Produit.objects.get(id=produitId)
    commande, created = Commande.objects.get_or_create(client=client, complete=False)

    commandeItem, created = CommandeItem.objects.get_or_create(commande=commande, produit=produit)

    if action == 'add':
        commandeItem.quantite = (commandeItem.quantite + 1)
    elif action == 'remove':
        commandeItem.quantite = (commandeItem.quantite - 1)

    commandeItem.save()

    if commandeItem.quantite <= 0:
        commandeItem.delete()

    return JsonResponse('Item was added', safe=False)

# stripe.api_key = settings.STRIPE_SECRET_KEY
#
#
# class ProductLandingPageView(TemplateView):
#     template_name = "landing.html"
#
#
#
# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         YOUR_DOMAIN = "http://127.0.0.1:8000/"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': 2000,
#                         'product_data': {
#                             'name': 'Stubborn Attachements'
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })
