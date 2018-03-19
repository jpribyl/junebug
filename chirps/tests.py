from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.


from .models import Chirp


User = get_user_model()

class ChirpModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='jmitchel33333333333')

    def test_chirp_item(self):
        obj = Chirp.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        self.assertTrue(obj.content == "Some random content")
        self.assertTrue(obj.id == 1)
        #self.assertEqual(obj.id, 1)
        absolute_url = reverse("detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_chirp_url(self):
        obj = Chirp.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        absolute_url = reverse("detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
