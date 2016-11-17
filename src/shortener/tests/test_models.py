from django.test import TestCase

from shortener.models import Url


class TestModelUrl(TestCase):
    def setUp(self):
        self.urls = {
            'undefined': {
                'url': 'localhost'
            },
            'defined': {
                'url': 'localhost2',
                'short': 'tyrion'
            }
        }

        self.url_random_short = Url.objects.create(**self.urls['undefined'])
        self.url_defined_short = Url.objects.create(**self.urls['defined'])

    def test__str__(self):
        _str = self.url_defined_short.__str__()
        expected_str = '{}:{}'.format(self.urls['defined']['url'],
                                      self.urls['defined']['short'])

        self.assertEqual(_str, expected_str)

    def test_create_without_short(self):
        self.assertTrue(self.url_random_short.short)

    def test_create_with_short(self):
        self.assertEqual(self.url_defined_short.short,
                         self.urls['defined']['short'])

    def test_update_short(self):
        short = 'ju'
        self.url_random_short.short = short
        self.url_random_short.save()
        self.assertEqual(self.url_random_short.short, short)
