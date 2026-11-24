from pathlib import Path

contoh = Path(__file__).with_name("contoh_data.txt")
# Context manager with menutup berkas otomatis ketika blok selesai.
with contoh.open(encoding="utf-8") as berkas:
    baris = berkas.readline().strip()
print("Baris pertama:", baris)