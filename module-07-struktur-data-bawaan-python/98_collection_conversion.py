angka = [3, 1, 3, 2]

# Set menghilangkan duplikat; sorted mengembalikan urutan deterministik.
unik = set(angka)
print("List unik:", sorted(unik))
print("Tuple unik:", tuple(sorted(unik)))