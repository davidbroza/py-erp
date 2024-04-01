from django.test import TestCase
from erp.productsV2.models import Product


class TestProduct(TestCase):

    def test_product(self):
        product = Product.objects.create(name="Test Product")
        self.assertEqual(str(product), "Test Product")
