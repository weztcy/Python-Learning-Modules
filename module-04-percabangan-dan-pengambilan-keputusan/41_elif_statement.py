nilai = 82

# elif memeriksa kondisi berikutnya hanya ketika kondisi sebelumnya salah.
if nilai >= 90:
    kategori = "A"
elif nilai >= 75:
    kategori = "B"
else:
    kategori = "C"
print("Kategori:", kategori)