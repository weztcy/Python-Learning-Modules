buah = ["apel", "pisang", "jeruk"]
target = "pisang"

# Periksa keanggotaan sebelum index agar elemen yang tidak ada tidak memicu ValueError.
if target in buah:
    print("Indeks:", buah.index(target))
else:
    print("Tidak ditemukan")