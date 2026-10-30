angka = [1, 2, 3]

# map mengembalikan iterator hasil pemanggilan fungsi pada setiap elemen.
hasil = map(lambda nilai: nilai ** 2, angka)
print("Kuadrat:", list(hasil))