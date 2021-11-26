from django.shortcuts import render

from .models import Parametres


def base(request):
    parametres = Parametres.objects.first()
    return {'parametres': parametres}
