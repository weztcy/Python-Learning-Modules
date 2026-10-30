def urut(data):
    hasil = data.copy()
    for awal in range(len(hasil)):
        terkecil = awal
        # Cari minimum bagian tersisa, kemudian letakkan di posisi awal.
        for posisi in range(awal + 1, len(hasil)):
            if hasil[posisi] < hasil[terkecil]:
                terkecil = posisi
        hasil[awal], hasil[terkecil] = hasil[terkecil], hasil[awal]
    return hasil


print(urut([4, 1, 3, 2]))