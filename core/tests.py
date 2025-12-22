
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category, Product


class ProductAPITests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="smartphones",
        )
        self.product = Product.objects.create(
            name='Samsung_A30s',
            description='the best phone',
            price=99999999.99,
            category=self.category
        )
    
    def test_model_str(self):
        self.assertEqual(str(self.product), 'Samsung_A30s')



