import sys

sapaan = "Halo, 你好, مرحبا"

# String Python menyimpan karakter Unicode dari berbagai bahasa.
# UTF-8 diperlukan saat stdout Windows memakai encoding lama seperti cp1252.
sys.stdout.reconfigure(encoding="utf-8")
print(sapaan)
print("Jumlah karakter:", len(sapaan))