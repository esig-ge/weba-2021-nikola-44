# FERREIRA STOJKOVIC Nikola
from datetime import date, datetime, timedelta
import datetime as dt

from django.db import models
from compte.models import Client

# Create your models here.


class Prestation(models.Model):
    LONGEUR_CHEVEUX = (
        ('Courts', 'Courts'),
        ('Longs', 'Longs'),
        ('/', '/')
    )
    STATUT = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    nom = models.CharField(max_length=60)
    pour = models.CharField(max_length=6, choices=LONGEUR_CHEVEUX, default='')
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    duree = models.TimeField()
    # statut = models.CharField()

    def __str__(self):
        if self.pour == '/':
            return self.nom
        else:
            return self.nom + ' --- ' + self.pour


class Reservation(models.Model):
    TRANCHE_HORAIRES = [(dt.time(hour=x, minute=y), '{:02d}:{:02d}'.format(x, y)) for x in range(8, 18) for y in range(0, 60, 30)]
    #     (
    #     ('08:00', '08:00'),
    #     ('08:30', '08:30'),
    #     ('09:00', '09:00'),
    #     ('09:30', '09:30'),
    #     ('10:00', '10:00'),
    #     ('10:30', '10:30'),
    #     ('11:00', '11:00'),
    #     ('11:30', '11:30'),
    #     ('12:00', '12:00'),
    #     ('12:30', '12:30'),
    #     ('13:00', '13:00'),
    #     ('13:30', '13:30'),
    #     ('14:00', '14:00'),
    #     ('14:30', '14:30'),
    #     ('15:00', '15:00'),
    #     ('15:30', '15:30'),
    #     ('16:00', '16:00'),
    #     ('16:30', '16:30'),
    #     ('17:30', '17:30'),
    # )
    date = models.DateField('Date: JJ.MM.AAAA ', auto_now_add=False, null=True, blank=True)  # date par défaut aujourd'hui
    heure = models.TimeField('Heure: HH:MM (H+1)', auto_now_add=False, null=True, blank=True, choices=TRANCHE_HORAIRES)  # date par défaut aujourd'hui
    commentaire = models.TextField(blank=True, default='')
    prestations = models.ManyToManyField(Prestation, through='ResPres')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    # statut réservation

    def __str__(self):
        return 'Réservation du ' + self.date.__str__() + self.heure.__str__()

    def is_past_due(self):
        return datetime.now().astimezone() > datetime.combine(datetime.date(self.date.value_from_object(self)), datetime.time(self.heure.value_from_object(self)))

    def heure_fin(self):
        hf = self.heure
        print('Voila la liste des prestations', self.prestations)
        if self.prestations.all():
            for prestation in self.prestations.all():
                hf = datetime.combine(self.date, self.heure) - timedelta(hours=prestation.duree.hour, minutes=prestation.duree.minute)
            return hf
        else:
            return self.heure


class ResPres(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True, null=True)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE, blank=True, null=True)
    duree_effective = models.TimeField(blank=True, null=True, default='00:00')
    prix = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = [['reservation', 'prestation']]
