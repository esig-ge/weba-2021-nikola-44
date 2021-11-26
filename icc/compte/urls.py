# Châtelain Dorian
from django.urls import path
from . import views
from django.contrib import admin

# app_name = 'compte'

urlpatterns = [
    path('inscription', views.inscriptionPage, name='inscription'),
    path('acces', views.accesPage, name='acces'),
    path('quitter', views.logoutUser, name='quitter'),
    path('gererClients/', views.gererClient, name='gererClient'),
    path('supprimer_client/<str:pk>', views.supprimer_client, name='supprimer_client'),
    path('profile/', views.profile, name='profile'),
    path('<str:pk>/', views.modifier_client, name='modifier_client'),

]