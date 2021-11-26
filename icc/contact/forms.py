from django import forms
from .models import Contact


# Create your forms here.
class ContactForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    adresse_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=150)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=2000)
