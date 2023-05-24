from http import HTTPStatus

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from logistic.models import Product


class TestLogistic(APITestCase):
    fixtures = ['products.json']

    def test_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        products = list(Product.objects.all()[:10].values())
        response_data = response.json().get('results')
        self.assertEquals(len(response_data), len(products), 'Length of response data does not match expected data\n'
                                                             f'Length of response data is {len(response_data)}\n'
                                                             f'Length of expected data is {len(products)}')
        self.assertEquals(response_data, products, 'Response data does not match expected data\n'
                                                   f'Response data is {response_data}\n'
                                                   f'Expected data is {products}')
