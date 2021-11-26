from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'date_commande': forms.DateTimeField(),
            'complete': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_commande': forms.TextInput(attrs={'class': 'form-control'}),
        }
