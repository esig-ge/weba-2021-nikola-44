from django.test import TestCase
from reservations.models import Prestation, ResPres, Reservation
from compte.models import Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve


class TestViews(TestCase):

    def setUp(self):
        # User.objects.create(username='admin', password='1234', is_staff=True)
        # self.login = self.client.login(username='admin', password='1234')

        self.user = User.objects.create_user(username='admin', password='1234', is_staff=True)
        self.user.save()
        self.login = self.client.login(username='admin', password='1234')

        self.prestation1 = Prestation.objects.create(nom="Balayage ou Mèches", prix="40", pour="/", duree="01:30")
        self.prestation2 = Prestation.objects.create(nom="Brushing", prix="50", pour="Courts", duree="00:30")
        self.prestation3 = Prestation.objects.create(nom="Brushing", prix="65", pour="Longs", duree="01:00")
        self.prestation4 = Prestation.objects.create(nom="Chignon", prix="68", pour="Courts", duree="00:45")
        self.prestation5 = Prestation.objects.create(nom="Chignon", prix="94", pour="Longs", duree="01:15")

        # refractor
        user = User.objects.create()
        client = Client.objects.create(user=user, nom="nom", prenom="prenom", dateNaissance='1993-05-25', telephone="0256489756", genre="Autre")
        self.reservation1 = Reservation.objects.create(date='2022-01-25', heure='10:00:00', commentaire="commentaire", client=client)
        self.respres1 = ResPres.objects.create(reservation=self.reservation1, prestation=self.prestation3)

        self.reservation2 = Reservation.objects.create(date='2022-01-25', heure='13:00:00', commentaire="commentaire", client=client)
        self.respres2 = ResPres.objects.create(reservation=self.reservation2, prestation=self.prestation5)

        self.reservation3 = Reservation.objects.create(date='2022-01-25', heure='14:00:00', commentaire="commentaire", client=client)
        self.respres3 = ResPres.objects.create(reservation=self.reservation3, prestation=self.prestation5)

    # aide par Michael
    def test_bon_template_appele(self):
        reponse = self.client.get("/reservations/prestations-tdd/")
        self.assertTemplateUsed(reponse, template_name="reservations/admin/prestations-tdd.html")

    # j'ai créé 5 prestations auparavant
    def test_affiche_une_liste(self):
        response = self.client.get('/reservations/prestations-tdd/')
        self.assertTrue(len(response.context['prestations']) > 0)
        # refractor
        self.assertTrue(response.context['prestations'][0] == self.prestation5)
        self.assertTrue(response.context['prestations'][1] == self.prestation3)

    # aidé par Edona
    def test_connexion_admin(self):
        self.assertTrue(self.login)
