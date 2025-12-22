import pytest
from rest_framework import status
from .models import Product, Category

@pytest.fixture
def test_category():
    pass

def test_product(test_category):
    pass

@pytest.mark.django_db
def test_list_products(client, test_product):
    pass



