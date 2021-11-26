# Châtelain Dorian
from django.urls import path
from . import views
from django.contrib import admin

appname = 'commande'

urlpatterns = [
    path('gererCommandes/', views.gererCommande, name='gererCommande'),
    path('<str:pk>/', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<str:pk>', views.supprimer_commande, name='supprimer_commande'),
]
