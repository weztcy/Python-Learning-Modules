class Inventaris:
    def __init__(self):
        self.stok = {}

    def tambah(self, barang, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.stok[barang] = self.stok.get(barang, 0) + jumlah

    def ambil(self, barang, jumlah):
        if jumlah <= 0 or jumlah > self.stok.get(barang, 0):
            raise ValueError("Stok tidak mencukupi atau jumlah tidak valid")
        self.stok[barang] -= jumlah


if __name__ == "__main__":
    inventaris = Inventaris()
    inventaris.tambah("Buku", 10)
    inventaris.ambil("Buku", 3)
    print("Stok:", inventaris.stok)