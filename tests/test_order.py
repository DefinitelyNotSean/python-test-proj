import unittest
from unittest.mock import Mock, patch
from store.orders.order import Order
from store.customers.customer import Customer
from store.products.product import Product
from store.payments.payment_processor import PaymentProcessor
from unittest.mock import patch, MagicMock

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "john.doe@example.com")
        self.product1 = Product(1, "Product 1", 10)
        self.product2 = Product(2, "Product 2", 20)
        self.order = Order(1, self.customer, [self.product1, self.product2])

    def test_order_total_amount(self):
        total_amount = self.order.get_total_amount()
        self.assertEqual(total_amount, 30)

if __name__ == "__main__":
    unittest.main()
