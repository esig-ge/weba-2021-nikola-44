# Dorian Châtelain

from django import forms
from .models import Parametres


class SalonForm(forms.ModelForm):
    class Meta:
        model = Parametres
        fields = ['nomSalon', 'telephone', 'adresse', 'codePostal', 'mail', 'stockMinPVente', 'prixLivraison']
        widgets = {
            'stockMinPVente': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'prixLivraison': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'type' : 'number'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'codePostal': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'nomSalon': forms.TextInput(attrs={'class': 'form-control'}),
        }
