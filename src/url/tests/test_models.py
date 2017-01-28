from django.test import TestCase

from url.models import URL


class TestUrlModel(TestCase):
    def setUp(self):
        self.url = URL(id=123, url='example.com')

    def test_short(self):
        self.assertEqual(self.url.short, '1z')
