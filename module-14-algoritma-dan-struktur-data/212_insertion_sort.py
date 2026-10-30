def urut(data):
    hasil = data.copy()
    for indeks in range(1, len(hasil)):
        nilai, posisi = hasil[indeks], indeks - 1
        # Geser elemen besar sebelum memasukkan nilai ke bagian terurut.
        while posisi >= 0 and hasil[posisi] > nilai:
            hasil[posisi + 1] = hasil[posisi]
            posisi -= 1
        hasil[posisi + 1] = nilai
    return hasil


print(urut([4, 1, 3, 2]))