class Produk:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        print(f"Produk: {self.merek} ({self.tahun})")
        
class Komputer(Produk):
    def __init__(self, merek, tahun, jenis):
        super().__init__(merek, tahun)
        self.jenis = jenis
        
    def info(self):
        print(f"Komputer: {self.merek} ({self.tahun}) - Jenis: {self.jenis}")
        
class Handphone(Produk):
    def __init__(self, merek, tahun, sistem_operasi):
        super().__init__(merek, tahun)
        self.sistem_operasi = sistem_operasi
        
    def info(self):
        print(f"Handphone: {self.merek} ({self.tahun}) - Sistem Operasi: {self.sistem_operasi}")