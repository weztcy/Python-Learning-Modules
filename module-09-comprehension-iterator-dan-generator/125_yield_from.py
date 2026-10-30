def gabungkan():
    # yield from meneruskan setiap elemen dari iterable ke pemanggil.
    yield from (1, 2)
    yield from (3, 4)


print("Gabungan:", list(gabungkan()))