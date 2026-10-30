def urut(data):
    hasil = data.copy()
    for batas in range(len(hasil) - 1, 0, -1):
        for indeks in range(batas):
            # Tukar dua tetangga jika salah urut; terbesar menuju ujung.
            if hasil[indeks] > hasil[indeks + 1]:
                hasil[indeks], hasil[indeks + 1] = hasil[indeks + 1], hasil[indeks]
    return hasil


print(urut([4, 1, 3, 2]))