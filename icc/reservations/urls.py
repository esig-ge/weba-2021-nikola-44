# FERREIRA STOJKOVIC Nikola
from django.urls import path
from . import views

# appname = 'reservations'


urlpatterns = [
    # path('planning-visiteurs/', views.planning_visiteurs, name='planning-visiteurs'),
    # path('planning-clients/', views.planning_clients, name='planning-clients'),
    path('planning/', views.planning, name='planning'),


    # path('rendezvous/', views.rendezvous, name='rendezvous'),

    path('prestations/', views.prestations, name='prestations'),
    path('admin/prestations/', views.prestations_admin, name='prestations-admin'),

    path('ajouter-reservation/', views.ajouter_reservation, name='ajouter-reservation'),
    path('supprimer-reservation-<int:id>/', views.supprimer_reservation, name='supprimer-reservation'),
    path('mes-reservations/', views.mes_reservations, name='mes-reservations'),
    path('reservations/', views.reservations, name='reservations'),

    path('admin/ajouter-prestation/', views.ajouter_prestation, name='ajouter-prestation'),
    path('admin/modifier-prestation-<int:id>/', views.modifier_prestation, name='modifier-prestation'),
    path('admin/supprimer-prestation-<int:id>/', views.supprimer_prestation, name='supprimer-prestation'),
    # path('reserver/', views.reserver, name='reserver'),
    path('test/', views.test, name='test'),
    path('test-prestations/', views.test_prestations, name='test-prestation'),
    # path('<int:jour>/', views.test, name='test-jour')

]
