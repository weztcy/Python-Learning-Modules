def urut(data):
    if len(data) <= 1:
        return data[:]
    tengah = len(data) // 2
    kiri, kanan = urut(data[:tengah]), urut(data[tengah:])
    hasil = []
    i = j = 0
    # Gabungkan dua sub-list terurut dengan dua indeks agar tidak menggeser list.
    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    return hasil + kiri[i:] + kanan[j:]


print(urut([4, 1, 3, 2]))