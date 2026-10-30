import os

# os membaca informasi sistem; getenv memakai default jika variabel belum tersedia.
print("Pemisah path:", os.sep)
print("Variabel contoh:", os.getenv("CONTOH_PYTHON", "belum diatur"))