# # Dorian Chatelain
from django.urls import path

from . import views
from .views import CheckoutPageView

urlpatterns = [
    path('', CheckoutPageView.as_view(), name='checkout'),
    path('charge/', views.charge, name='charge'),
]
