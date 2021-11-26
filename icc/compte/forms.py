# Châtelain Dorian
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client


class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'dateNaissance', 'telephone', 'genre', 'commentaire')
        widgets={
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        }


class ProfileModifierForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'dateNaissance', 'telephone', 'genre')
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'dateNaissance': forms.TextInput(attrs={'class': 'form-control', 'value': Client.dateNaissance}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'genre': forms.Select(attrs={'class': 'form-control'}, choices=Client.GENRES),
        }


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('commentaire',)
        widgets = {
            'commentaire': forms.TextInput(attrs={'class': 'form-control'})
        }

