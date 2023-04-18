class Order:
    def __init__(self, id, customer, products):
        self.id = id
        self.customer = customer
        self.products = products

    def get_total_amount(self):
        return sum(product.price for product in self.products)
