class Produk:
    def __init__(self, harga):
        self.harga = harga

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        # Setter menjaga nilai tetap valid saat instance dibuat maupun diperbarui.
        if nilai < 0:
            raise ValueError("Harga tidak boleh negatif")
        self._harga = nilai


produk = Produk(50)
produk.harga = 75
print("Harga:", produk.harga)