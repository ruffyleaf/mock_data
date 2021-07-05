import random

class ProductGenerator:

    def __init__(self, products):
        self.fruit = random.choice(products)
        self.quantity = abs(int(random.gauss(10.0, 9.0)))
    
    def create_order_id(self):
        self.order_id = random.randint(3, 9)