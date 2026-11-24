def tagihan(keranjang):
    total = 0
    for nama, harga, jumlah in keranjang:
        if harga < 0 or jumlah <= 0:
            raise ValueError(f"Item tidak valid: {nama}")
        total += harga * jumlah
    return total


if __name__ == "__main__":
    # Harga berupa integer rupiah menghindari kesalahan pembulatan float sederhana.
    print("Total belanja:", tagihan([("Buku", 10000, 2), ("Pensil", 2000, 3)]))