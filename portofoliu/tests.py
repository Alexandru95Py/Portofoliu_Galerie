from django.test import TestCase
from django.urls import reverse
from .models import Proiect

class PortofoliuHomeViewTest(TestCase):
    def setUp(self):
        self.proiect = Proiect.objects.create(
            titlu="Test Proiect",
            descriere="Descriere test proiect",
            categorie="picturi",
            link="https://example.com"
        )

    def test_portofoliu_home_status_code(self):
        response = self.client.get(reverse('portofoliu_home'))
        self.assertEqual(response.status_code, 200)

    def test_portofoliu_home_content(self):
        response = self.client.get(reverse('portofoliu_home'))
        self.assertContains(response, "Test Proiect")
        self.assertContains(response, "Descriere test proiect")

class PortofoliuCategorieViewTest(TestCase):
    def setUp(self):
        self.proiect = Proiect.objects.create(
            titlu="Test Proiect",
            descriere="Descriere test proiect",
            categorie="picturi",
            link="https://example.com"
        )

    def test_portofoliu_categorie_status_code(self):
        response = self.client.get(reverse('portofoliu_picturi'))
        self.assertEqual(response.status_code, 200)

    def test_portofoliu_categorie_content(self):
        response = self.client.get(reverse('portofoliu_picturi'))
        self.assertContains(response, "Test Proiect")
        self.assertContains(response, "Descriere test proiect")

class ProiectModelTest(TestCase):
    def test_proiect_str(self):
        proiect = Proiect.objects.create(
            titlu="Test Proiect",
            descriere="Descriere test proiect",
            categorie="picturi",
            link="https://example.com"
        )
        self.assertEqual(str(proiect), "Test Proiect")
