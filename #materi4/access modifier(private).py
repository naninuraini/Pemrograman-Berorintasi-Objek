class Mobil:
    def __init__(self, merek, tahun):
        self._merek = merek
        self._tahun = tahun
        
    def info(self):
        print(f"Mobil: {self._merek} ({self._tahun})")
        
mobil1 = Mobil("Toyota", 2020)
print(mobil1._merek)  # output: Toyota
mobil1.info()         # output: Mobil: Toyota (2020)

