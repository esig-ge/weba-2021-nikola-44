from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from reservations.test.test_views import TestViews


class TestUrls(TestCase):

    # aidé par Edona
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='1234', is_staff=True)
        self.user.save()
        self.client.login(username='admin', password='1234')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reservations/prestations-tdd/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('prestations-tdd'))
        self.assertEqual(response.status_code, 200)

