import unittest
from store.products import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Test Product", 50)

    def test_product_creation(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 50)

if __name__ == "__main__":
    unittest.main()
