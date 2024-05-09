class Smartphone:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand
        
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        self._year = year
        
smartphone1 = Smartphone("Samsung", 2020)
print(smartphone1.get_brand())  
smartphone1.set_brand("Apple")
print(smartphone1.get_brand())  
print(smartphone1.get_year())   
smartphone1.set_year(2022)
print(smartphone1.get_year())   
