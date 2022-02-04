import operator
import unittest

from django.db.models import Count
from django.test import TestCase
from compte.models import Client, User
from reservations.models import Prestation, ResPres, Reservation
from django.urls import reverse, resolve


class TestModels(TestCase):

    def test_saving_and_retrieving_items(self):
        prestation1 = Prestation.objects.create(nom="Brushing", prix="65", pour="Longs", duree="01:00")
        prestation1.save()

        prestation2 = Prestation.objects.create(nom="Chignon", prix="94", pour="Longs", duree="01:15")
        prestation2.save()

        saved_item = Prestation.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item, prestation1)
        self.assertEqual(second_saved_item, prestation2)

    def test_delete_items(self):
        print('objets existant', Prestation.objects.all())

        prestation1 = Prestation.objects.create(nom="Brushing", prix="65", pour="Longs", duree="01:00")
        prestation1.save()

        prestation2 = Prestation.objects.create(nom="Chignon", prix="94", pour="Longs", duree="01:15")
        prestation2.save()

        saved_item = Prestation.objects.all()
        self.assertEqual(saved_item.count(), 2)

        prestation1.delete()
        prestation2.delete()

        self.assertEqual(saved_item.count(), 0)

    def test_has_attribute(self):
        self.assertTrue(hasattr(Prestation(), 'nom'))
        self.assertTrue(hasattr(Prestation(), 'pour'))

    @unittest.expectedFailure
    def test_no_dupplicate(self):
        prestation1 = Prestation.objects.create(nom="Brushing", prix="65", pour="Longs", duree="01:00")
        prestation1.save()

        prestation2 = Prestation.objects.create(nom="Brushing", prix="65", pour="Longs", duree="01:00")
        prestation2.save()

        print(Prestation.objects.values('nom', 'pour').annotate(name_count=Count('nom')).filter(name_count__gt=1))
        compteur = len(Prestation.objects.values('nom', 'pour'))
        print('compteur', compteur)
        self.assertEqual(compteur, 0)


