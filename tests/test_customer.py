import unittest
from store.customers.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "john.doe@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.id, 1)
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john.doe@example.com")

if __name__ == "__main__":
    unittest.main()
