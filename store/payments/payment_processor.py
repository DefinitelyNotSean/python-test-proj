import requests

class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    def charge_customer(self, customer, amount):
        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"customer_id": customer.id, "amount": amount},
        )
        return response.status_code == 201
