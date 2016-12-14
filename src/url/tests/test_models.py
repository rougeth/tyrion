from django.test import TestCase

from url.models import Url


class TestUrlModel(TestCase):
    def setUp(self):
        self.url = Url(id=123, url='example.com')

    def test__str__(self):
        _str = self.url.__str__()
        expected_str = '{}:{}'.format(self.url.url, self.url.short)

        self.assertEqual(_str, expected_str)

    def test_short(self):
        self.assertEqual(self.url.short, '1z')
