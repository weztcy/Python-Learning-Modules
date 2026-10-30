class Kotak:
    def __init__(self, isi):
        self.isi = isi

    def __len__(self):
        # len(instance) memanggil __len__ secara implisit.
        return len(self.isi)

    def __contains__(self, barang):
        return barang in self.isi


kotak = Kotak(["buku", "pensil"])
print("Jumlah:", len(kotak), "Ada buku:", "buku" in kotak)