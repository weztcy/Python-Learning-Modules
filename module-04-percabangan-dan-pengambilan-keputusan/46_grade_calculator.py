nilai = 86

# Periksa batas tertinggi lebih dulu agar hanya satu kategori terpilih.
if not 0 <= nilai <= 100:
    print("Nilai harus antara 0 dan 100")
elif nilai >= 85:
    print("Grade: A")
elif nilai >= 70:
    print("Grade: B")
elif nilai >= 55:
    print("Grade: C")
else:
    print("Grade: D")