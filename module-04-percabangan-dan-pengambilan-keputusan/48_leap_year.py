tahun = 2024

# Tahun abad hanya kabisat jika habis dibagi 400; selain itu cukup dibagi 4.
kabisat = tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)
print(tahun, "kabisat" if kabisat else "bukan kabisat")