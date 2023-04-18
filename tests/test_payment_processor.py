import unittest
from unittest.mock import Mock, patch
from store.orders.order import Order
from store.customers.customer import Customer
from store.products.product import Product
from store.payments.payment_processor import PaymentProcessor
from unittest.mock import patch

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

    @patch("store.payments.payment_processor.requests.post")
    def test_charge_customer_requests(self, mock_requests_post):
        # Create a custom response object with the desired status code
        response = Mock()
        response.status_code = 201

        # Set the mock_requests_post return value to the custom response object
        mock_requests_post.return_value = response

        payment_processor = PaymentProcessor("api_key")
        payment_successful = payment_processor.charge_customer(self.customer, self.order.get_total_amount())

        self.assertTrue(payment_successful)
        mock_requests_post.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/posts",
            headers={"Authorization": f"Bearer {payment_processor.api_key}"},
            json={"customer_id": self.customer.id, "amount": self.order.get_total_amount()},
        )

if __name__ == "__main__":
    unittest.main()
