import unittest
from unittest.mock import Mock, patch
from store.orders import Order
from store.customers import Customer
from store.products import Product
from store.payments import PaymentProcessor


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "john.doe@example.com")
        self.product1 = Product(1, "Product 1", 10)
        self.product2 = Product(2, "Product 2", 20)
        self.order = Order(1, self.customer, [self.product1, self.product2])

    def test_order_total_amount(self):
        total_amount = self.order.get_total_amount()
        self.assertEqual(total_amount, 30)


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "john.doe@example.com")
        self.order = Order(1, self.customer, [Product(1, "Product 1", 10), Product(2, "Product 2", 20)])

    @patch("store.payments.payment_processor.PaymentProcessor.charge_customer")
    def test_charge_customer(self, mock_charge_customer):
        mock_charge_customer.return_value = True

        payment_processor = PaymentProcessor("api_key")
        payment_successful = payment_processor.charge_customer(self.customer, self.order.get_total_amount())

        self.assertTrue(payment_successful)
        mock_charge_customer.assert_called_once_with(self.customer, self.order.get_total_amount())


if __name__ == "__main__":
    unittest.main()
