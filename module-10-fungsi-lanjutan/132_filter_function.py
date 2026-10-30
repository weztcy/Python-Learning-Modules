angka = [1, 2, 3, 4, 5]

# filter mempertahankan elemen yang membuat fungsi predicate bernilai benar.
genap = filter(lambda nilai: nilai % 2 == 0, angka)
print("Genap:", list(genap))