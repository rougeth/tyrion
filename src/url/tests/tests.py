import json

from django.test import TestCase
from django.urls import reverse

from url.models import Url


class URLAPITest(TestCase):
    # This class still need refactoring :/

    def setUp(self):
        self.url = Url.objects.create(id=123, url='http://localhost')

    def test_create_new_url(self):
        create_short_url = reverse('api_url_list')

        data = {
            'url': 'http://example.com'
        }

        response = self.client.post(create_short_url, json.dumps(data),
                                    content_type='application/json')

        # Test api response
        response_json = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['url'], data['url'])
        self.assertEqual(response_json['short'], '20')

        # Test database content
        url = Url.objects.last()
        self.assertEqual(url.url, data['url'])
        self.assertEqual(url.short, '20')

    def test_list_urls(self):
        list_urls = reverse('api_url_list')
        response = self.client.get(list_urls)

        # Test api response
        response_json = response.json()['objects']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0]['url'], 'http://localhost')
        self.assertEqual(response_json[0]['short'], '1z')

        # Test database content
        url = Url.objects.last()
        self.assertEqual(url.url, self.url.url)
        self.assertEqual(url.short, self.url.short)

    def test_detail_url(self):
        detail_url = reverse('api_url_detail', args=[self.url.short])
        response = self.client.get(detail_url)

        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['url'], 'http://localhost')
        self.assertEqual(response_json['short'], '1z')

    def test_delete_url(self):
        delete_url = reverse('api_url_detail', args=[self.url.short])
        response = self.client.delete(delete_url)

        # Test api response
        self.assertEqual(response.status_code, 204)

        # Test database content
        self.assertFalse(Url.objects.filter(id=self.url.id).exists())
