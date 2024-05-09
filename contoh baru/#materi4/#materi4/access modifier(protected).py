class Smartphone:
    def __init__(self, brand, year, model):
        self.__brand = brand
        self.__year = year
        self.__model = model
        
    def info(self):
        print(f"Smartphone: {self.__brand} ({self.__year}), Model: {self.__model}")

class Flagship(Smartphone):
    def __init__(self, brand, year, model, features):
        super().__init__(brand, year, model)
        self.__features = features
        
    def info(self):
        super().info()
        print(f"Features: {self.__features}")

flagship1 = Flagship("Apple", 2021, "iPhone 13 Pro", "5G, A15 Bionic, ProMotion display")
flagship1.info()
