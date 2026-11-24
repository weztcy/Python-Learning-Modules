def urut(data):
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2]
    # Pisahkan nilai kecil, sama, dan besar agar duplikat tetap terjaga.
    kiri = [nilai for nilai in data if nilai < pivot]
    sama = [nilai for nilai in data if nilai == pivot]
    kanan = [nilai for nilai in data if nilai > pivot]
    return urut(kiri) + sama + urut(kanan)


print(urut([4, 1, 3, 2, 3]))