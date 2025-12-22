import pytest
from rest_framework import status
from .models import Product, Category

@pytest.fixture
def test_category():
    return Category.objects.create(
        name='Smarthphone',
    )

def test_product(test_category):
    return Product.objects.create(
        name = 'Redmi 12',
        description = 'Made in China',
        price = 99999999.99,
        category = test_category
    )

@pytest.mark.django_db
def test_list_products(client, test_products):
    response = client.get('/api/products')
    assert response.status_code == status.HTTP_200_OK



