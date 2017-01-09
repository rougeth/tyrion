from django.test import TestCase
from django.urls import reverse

from url.models import URL


class TestURLViews(TestCase):
    def setUp(self):
        self.url = URL.objects.create(id=1, url='example.com')

    def test_404(self):
        url = reverse('url_redirect', kwargs={'short': '404'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_redirect(self):
        url = reverse('url_redirect', kwargs={'short': '1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.url.url)
