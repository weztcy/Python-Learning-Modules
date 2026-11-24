def cari(data, target):
    kiri, kanan = 0, len(data) - 1
    # Data harus terurut: tiap langkah membuang setengah rentang pencarian.
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah
        if data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1


print("Indeks 7:", cari([1, 3, 5, 7, 9], 7))