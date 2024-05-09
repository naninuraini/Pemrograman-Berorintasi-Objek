class Mobil:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        
    def info(self):
        print(f"Mobil: {self.merek} ({self.tahun})")
        
mobil1 = Mobil("Toyota", 2020)
print(mobil1.merek)  # output: Toyota
mobil1.info()        # output: Mobil: Toyota (2020)

