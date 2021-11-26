# Zumeri Faton
from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Message de la part d'un client"
            body = {
            'name': form.cleaned_data['nom'],
            'email_address': form.cleaned_data['adresse_email'],
            'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'email_address', ['catisacoiffure@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('contact')

    form = ContactForm()
    return render(request, "contact.html", {'form':form})
