# Zumeri Faton
from django.db import models


# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.nom
