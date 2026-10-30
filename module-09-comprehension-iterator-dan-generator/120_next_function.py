angka = iter([10, 20])

# Argumen default pada next menghindari StopIteration saat data habis.
print(next(angka, "habis"))
print(next(angka, "habis"))
print(next(angka, "habis"))