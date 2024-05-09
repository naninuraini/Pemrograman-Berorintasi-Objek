class Smartphone:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        
    def info(self):
        print(f"Smartphone: {self._brand} {self._model} ({self._year})")

smartphone1 = Smartphone("Samsung", "Galaxy S21", 2021)
print(smartphone1._brand) 
smartphone1.info()         