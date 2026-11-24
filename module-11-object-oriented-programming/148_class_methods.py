class Produk:
    pajak = 0.11

    @classmethod
    def dari_teks(cls, teks):
        # cls membuat instance dari class pemanggil, bukan class yang ditulis tetap.
        return cls(int(teks))

    def __init__(self, harga):
        self.harga = harga


print("Harga:", Produk.dari_teks("100").harga)