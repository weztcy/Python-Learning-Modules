from functools import reduce

# reduce menggabungkan nilai akumulator dan elemen berikutnya sampai tersisa satu hasil.
hasil = reduce(lambda total, angka: total * angka, [1, 2, 3, 4], 1)
print("Hasil perkalian:", hasil)