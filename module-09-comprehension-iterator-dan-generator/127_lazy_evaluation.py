def kuadrat(data):
    for angka in data:
        print("Menghitung:", angka)
        yield angka ** 2


# Membuat generator belum menjalankan badan fungsi; next baru memintanya bekerja.
hasil = kuadrat(range(1, 4))
print("Generator dibuat")
print("Pertama:", next(hasil))
print("Kedua:", next(hasil))