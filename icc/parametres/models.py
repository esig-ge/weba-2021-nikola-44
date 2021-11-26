# Dorian Châtelain
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Parametres(models.Model):
    stockMinPVente = models.PositiveIntegerField()
    prixLivraison = models.PositiveIntegerField()
    telephone = models.CharField(max_length=100)
    adresse = models.CharField(max_length=30)
    codePostal = models.CharField(max_length=15)
    mail = models.CharField(max_length=50)
    nomSalon = models.CharField(max_length=150)

    def __str__(self):
        return self.nomSalon

    # def save(self, *args, **kwargs):
    #     if not self.pk and Parametres.objects.exists():
    #     # if you'll not check for self.pk
    #     # then error will also raised in update of exists model
    #         raise ValidationError("Il ne peut y avoir qu'un seul parametre")
    #     if self.pk:
    #         return super(Parametres, self).save(*args, **kwargs)
