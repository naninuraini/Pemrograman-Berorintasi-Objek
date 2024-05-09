# Konstruktor dan Destruktor untuk PenjualanAlatElektronik
class PenjualanAlatElektronik:
    # Atribut kelas
    total_penjualan = 0

    # Konstruktor
    def __init__(self, nama_barang, harga, jumlah_terjual):
        self.nama_barang = nama_barang
        self.harga = harga
        self.jumlah_terjual = jumlah_terjual
        PenjualanAlatElektronik.total_penjualan += jumlah_terjual

    # Metode objek
    def total_pendapatan(self):
        return self.harga * self.jumlah_terjual

    # Destruktor
    def __del__(self):
        PenjualanAlatElektronik.total_penjualan -= self.jumlah_terjual

barang1 = PenjualanAlatElektronik("Laptop", 8000000, 10)
barang2 = PenjualanAlatElektronik("Smartphone", 3000000, 20)

print(barang1.nama_barang)
print(barang2.total_penjualan)
del barang1
print(PenjualanAlatElektronik.total_penjualan)
