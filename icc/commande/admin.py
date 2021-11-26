from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Commande)
admin.site.register(CommandeItem)
admin.site.register(AdresseCommande)