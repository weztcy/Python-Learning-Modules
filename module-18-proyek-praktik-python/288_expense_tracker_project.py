class Pengeluaran:
    def __init__(self):
        self.catatan = []

    def tambah(self, kategori, jumlah):
        if jumlah <= 0:
            raise ValueError("Pengeluaran harus positif")
        self.catatan.append((kategori, jumlah))

    def total(self):
        return sum(jumlah for _, jumlah in self.catatan)


if __name__ == "__main__":
    buku = Pengeluaran()
    buku.tambah("Makan", 25000)
    buku.tambah("Transport", 10000)
    print("Total pengeluaran:", buku.total())