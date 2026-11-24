def angka():
    yield 1
    # Eksekusi dilanjutkan dari sini setelah next dipanggil lagi.
    yield 2


generator = angka()
print("Nilai pertama:", next(generator))
print("Nilai kedua:", next(generator))