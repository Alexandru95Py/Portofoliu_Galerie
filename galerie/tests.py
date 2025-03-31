from django.test import TestCase
from django.urls import reverse
from .models import Tablou, Comentariu, Like
from django.contrib.auth.models import User

class GalerieHomeViewTest(TestCase):
    def setUp(self):
        self.tablou = Tablou.objects.create(
            titlu="Test Tablou",
            descriere="Descriere test",
            imagine="tablouri/test.jpg"
        )

    def test_galerie_home_status_code(self):
        response = self.client.get(reverse('galerie_home'))
        self.assertEqual(response.status_code, 200)

    def test_galerie_home_content(self):
        response = self.client.get(reverse('galerie_home'))
        self.assertContains(response, "Test Tablou")
        self.assertContains(response, "Descriere test")

class TablouModelTest(TestCase):
    def test_tablou_str(self):
        tablou = Tablou.objects.create(
            titlu="Test Tablou",
            descriere="Descriere test",
            imagine="tablouri/test.jpg"
        )
        self.assertEqual(str(tablou), "Test Tablou")

class LikeFunctionalityTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.tablou = Tablou.objects.create(
            titlu="Test Tablou",
            descriere="Descriere test",
            imagine="tablouri/test.jpg"
        )

    def test_add_like(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('adauga_like', args=[self.tablou.id]))
        self.assertEqual(response.status_code, 200)
        self.tablou.refresh_from_db()
        self.assertEqual(self.tablou.likes, 1)

    def test_remove_like(self):
        self.client.login(username="testuser", password="testpassword")
        Like.objects.create(user=self.user, tablou=self.tablou)
        response = self.client.post(reverse('adauga_like', args=[self.tablou.id]))
        self.assertEqual(response.status_code, 200)
        self.tablou.refresh_from_db()
        self.assertEqual(self.tablou.likes, 0)

class CommentFunctionalityTest(TestCase):
    def setUp(self):
        self.tablou = Tablou.objects.create(
            titlu="Test Tablou",
            descriere="Descriere test",
            imagine="tablouri/test.jpg"
        )

    def test_add_comment(self):
        response = self.client.post(reverse('adauga_comentariu', args=[self.tablou.id]), {
            "name": "Test User",
            "text": "Acesta este un comentariu de test."
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comentariu.objects.filter(tablou=self.tablou, nume="Test User").exists())

    def test_add_comment_missing_fields(self):
        response = self.client.post(reverse('adauga_comentariu', args=[self.tablou.id]), {
            "name": "",
            "text": ""
        })
        self.assertEqual(response.status_code, 400)
