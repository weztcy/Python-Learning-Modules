def cari(data, target):
    # Cari satu per satu tanpa mensyaratkan data terurut.
    for indeks, nilai in enumerate(data):
        if nilai == target:
            return indeks
    return -1


print("Indeks 7:", cari([4, 7, 2], 7))