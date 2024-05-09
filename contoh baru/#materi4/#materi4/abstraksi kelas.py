from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def description(self):
        pass
    
class Laptop(Product):
    def description(self):
        print("This is a powerful laptop for your everyday computing needs.")
        
class Smartphone(Product):
    def description(self):
        print("Stay connected on the go with this sleek and feature-rich smartphone.")
        
laptop = Laptop()
laptop.description()  

smartphone = Smartphone()
smartphone.description() 
