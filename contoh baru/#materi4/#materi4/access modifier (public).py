class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def description(self):
        print(f"Product: {self.name} - Price: ${self.price}")

product1 = Product("Smartphone", 150)
print(product1.name)
product1.description()  