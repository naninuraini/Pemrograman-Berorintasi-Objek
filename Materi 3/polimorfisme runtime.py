class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        print(f"Kendaraan: {self.merek} ({self.tahun})")
        
class Mobil(Kendaraan):
    def __init__(self, merek, tahun, warna):
        super().__init__(merek, tahun)
        self.warna = warna

    def info(self):
        print(f"Mobil: {self.merek} ({self.tahun}) - Warna: {self.warna}")

class Sepeda(Kendaraan):
    def __init__(self, merek, tahun, jenis):
        super().__init__(merek, tahun)
        self.jenis = jenis
        
    def info(self):
        print(f"Sepeda: {self.merek} ({self.tahun}) - Jenis: {self.jenis}")

kendaraan1 = Kendaraan("Kendaraan", 2022)
mobil1 = Mobil("Toyota", 2020, "Merah")
sepeda1 = Sepeda("Polygon", 2021, "MTB")

kendaraan1.info()  # output: Kendaraan: Kendaraan (2022)
mobil1.info()      # output: Mobil: Toyota (2020) - Warna: Merah
sepeda1.info()     # output: Sepeda: Polygon (2021) - Jenis: MTB
