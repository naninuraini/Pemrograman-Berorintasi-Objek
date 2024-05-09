class Mobil:
    def __init__(self, merek, tahun):
        self.__merek = merek
        self.__tahun = tahun
        
    def info(self):
        print(f"Mobil: {self.__merek} ({self.__tahun})")
        
class Sport(Mobil):
    def __init__(self, merek, tahun, top_speed):
        super().__init__(merek, tahun)
        self.__top_speed = top_speed
        
    def info(self):
        super().info()
        print(f"Top speed: {self.__top_speed} km/h")
        
sport1 = Sport("Ferrari", 2021, 350)
# print(sport1.__merek)  # error: 'Sport' object has no attribute '__merek'
sport1.info()  # output: Mobil: Ferrari (2021)\nTop speed: 350 km/h

