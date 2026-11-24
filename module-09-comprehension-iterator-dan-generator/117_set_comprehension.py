angka = [1, 2, 2, 3, 3]

# Set comprehension menghasilkan nilai unik, tanpa menjamin urutan set.
kuadrat_unik = {nilai ** 2 for nilai in angka}
print("Kuadrat unik:", sorted(kuadrat_unik))