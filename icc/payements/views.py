# Dorian Châtelain
import stripe
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY



class CheckoutPageView(TemplateView):
    template_name = '../produits/templates/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutPageView, self).get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        # context.update({
        #     "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        # })
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='CHF',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, '../produits/templates/charge.html')
