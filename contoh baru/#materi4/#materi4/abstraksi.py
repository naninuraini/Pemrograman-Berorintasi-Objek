from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def price(self):
        pass

class Laptop(Product):
    def __init__(self, brand, model, specs):
        self.brand = brand
        self.model = model
        self.specs = specs
        
    def price(self):
        
        if self.brand == 'Apple':
            return 1500
        elif self.brand == 'Dell':
            return 1200
        else:
            return 1000 

class Smartphone(Product):
    def __init__(self, brand, model, features):
        self.brand = brand
        self.model = model
        self.features = features
        
    def price(self):
        
        if self.brand == 'Apple':
            return 1000
        elif self.brand == 'Samsung':
            return 900
        else:
            return 800  

laptop1 = Laptop('Apple', 'MacBook Pro', '16-inch, Core i7, 512GB SSD')
smartphone1 = Smartphone('Apple', 'iPhone 12', '5G, A14 Bionic, Dual Camera')

print("Harga laptop:", laptop1.price())  
print("Harga smartphone:", smartphone1.price())  
