#Constructor dan Destructor
#Penggunaan constructor
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

p = Manusia("John Doe", 25)
p.info()

#Penggunaan dectructor
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def __del__(self):
        print(f"{self.merek} {self.warna} dihapus")

mobil1 = Mobil("Toyota", "Merah")
del mobil1




