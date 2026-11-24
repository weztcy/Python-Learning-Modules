def hitung_tagihan(harga, jumlah):
    def subtotal():
        # Fungsi bersarang membantu membatasi perhitungan ini di lingkup pemanggilnya.
        return harga * jumlah

    return subtotal() + 2000


print("Tagihan termasuk ongkir:", hitung_tagihan(5000, 3))