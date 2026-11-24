# Generator expression menghasilkan nilai satu per satu saat sum memintanya.
kuadrat = (angka ** 2 for angka in range(1, 6))
print("Jumlah kuadrat:", sum(kuadrat))