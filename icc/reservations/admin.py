# FERREIRA STOJKOVIC Nikola
from django.contrib import admin
from .models import Reservation, Prestation, ResPres

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Prestation)
admin.site.register(ResPres)
