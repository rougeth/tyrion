import json

from django.test import TestCase
from django.urls import reverse

from .models import Url


class ShortURLTest(TestCase):
    def test__str__(self):
        url = 'localhost'
        hash = 'abc'
        u = Url(url=url, hash=hash)

        self.assertEqual(str(u), '{}:{}'.format(url, hash))

    def test_create_url(self):
        # need to test expected answer
        create_url_endpoint = reverse('api_url_list')
        data = {
            'url': 'localhost'
        }

        response = self.client.post(create_url_endpoint, json.dumps(data),
                                    content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_list_url(self):
        list_url_endpoint = reverse('api_url_list')

        response = self.client.get(list_url_endpoint,
                                   content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_detail_url(self):
        create_url_endpoint = reverse('api_url_list')
        data = {
            'url': 'localhost'
        }

        response = self.client.post(create_url_endpoint, json.dumps(data),
                                    content_type="application/json")
        pk = 1
        detail_url_endpoint = reverse('api_url_detail', args=(pk,))

        response = self.client.get(detail_url_endpoint,
                                   content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_delete_url(self):
        create_url_endpoint = reverse('api_url_list')
        data = {
            'url': 'localhost'
        }

        response = self.client.post(create_url_endpoint, json.dumps(data),
                                    content_type="application/json")
        pk = 1
        delete_url_endpoint = reverse('api_url_detail', args=(pk,))

        response = self.client.delete(delete_url_endpoint,
                                      content_type="application/json")

        self.assertEqual(response.status_code, 204)
