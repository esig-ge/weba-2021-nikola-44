# FERREIRA STOJKOVIC Nikola
import datetime

from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Prestation, Reservation
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


# class Rendezvous(forms.ModelForm):
#     # date = forms.DateField()
#     # heure = forms.TimeField()
#     # commentaire = forms.CharField(widget=forms.Textarea())
#
#     class Meta:
#         model = models.Reservation
#         fields = ['date_heure', 'commentaire']


class PrestationForm(ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'pour': forms.Select(attrs={'class': 'form-control'}),
            'prix': forms.TextInput(attrs={'class': 'form-control', 'type': 'decimal'}),
            'duree': forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'value': '00:00', 'step': '300'}),
        }


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'client': HiddenInput(),
            'commentaire': forms.Textarea(attrs={'class': 'form-control'}),
            'prestations': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date': forms.DateInput(format=datetime.datetime, attrs={'class': 'form-control', 'type': 'date'}),
            'heure': forms.Select(attrs={'class': 'form-control'}, choices=Reservation.TRANCHE_HORAIRES)
                   }
