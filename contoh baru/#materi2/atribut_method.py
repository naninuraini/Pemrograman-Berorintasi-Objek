# Atribut dan metode kelas untuk PenjualanAlatElektronik
class PenjualanAlatElektronik:
    # Atribut kelas
    total_penjualan = 0

    def __init__(self, nama_barang, harga, jumlah_terjual):
        self.nama_barang = nama_barang
        self.harga = harga
        self.jumlah_terjual = jumlah_terjual
        PenjualanAlatElektronik.total_penjualan += jumlah_terjual

    def tambah_penjualan(cls, jumlah):
        cls.total_penjualan += jumlah

    def reset_penjualan(cls):
        cls.total_penjualan = 0

barang1 = PenjualanAlatElektronik("Laptop", 8000000, 10)
barang2 = PenjualanAlatElektronik("Smartphone", 3000000, 20)

print(barang1.nama_barang)
print(barang2.total_penjualan)
PenjualanAlatElektronik.tambah_penjualan(5)
print(PenjualanAlatElektronik.total_penjualan)
PenjualanAlatElektronik.reset_penjualan()
print(barang1.total_penjualan)


# Instance atribut dan method objek untuk kelas PenjualanAlatElektronik
class PenjualanAlatElektronik:
    def __init__(self, nama_barang, harga, jumlah_terjual):
        self.nama_barang = nama_barang
        self.harga = harga
        self.jumlah_terjual = jumlah_terjual

    def total_pendapatan(self):
        return self.harga * self.jumlah_terjual

barang1 = PenjualanAlatElektronik("Laptop", 8000000, 10)
barang2 = PenjualanAlatElektronik("Smartphone", 3000000, 20)

print(barang1.nama_barang)
print(barang2.total_pendapatan())