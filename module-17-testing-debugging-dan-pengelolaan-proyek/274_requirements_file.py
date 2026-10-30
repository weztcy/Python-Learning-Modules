from pathlib import Path

# Baca file dependensi proyek; jangan instal paket secara otomatis saat demo.
path = Path(__file__).resolve().parent.parent / "requirements.txt"
paket = [baris for baris in path.read_text(encoding="utf-8").splitlines() if baris and not baris.startswith("#")]
print("Jumlah dependensi langsung:", len(paket))
print("Contoh:", paket[0])