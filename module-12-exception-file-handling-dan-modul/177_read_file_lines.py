from pathlib import Path

contoh = Path(__file__).with_name("contoh_data.txt")
# Iterasi berkas membaca satu baris per putaran tanpa memuat semua isi sekaligus.
with contoh.open(encoding="utf-8") as berkas:
    for nomor, baris in enumerate(berkas, 1):
        print(f"{nomor}: {baris.strip()}")