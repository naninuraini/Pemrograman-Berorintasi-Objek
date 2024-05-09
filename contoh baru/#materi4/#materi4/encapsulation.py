class Smartphone:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        
    def __info(self):
        print(f"Smartphone: {self._brand} ({self._year})")

smartphone1 = Smartphone("Samsung", 2020)
smartphone1._Smartphone__info()  # output: Smartphone: Sam
