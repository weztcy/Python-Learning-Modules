from pathlib import Path

# Path berdasarkan __file__ tidak bergantung pada direktori kerja terminal.
contoh = Path(__file__).with_name("contoh_data.txt")
with contoh.open(encoding="utf-8") as berkas:
    print("Isi file:", berkas.read().strip())