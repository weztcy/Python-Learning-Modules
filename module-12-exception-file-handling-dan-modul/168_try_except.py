# try menangani kesalahan konversi agar program tetap berjalan.
try:
    angka = int("bukan angka")
except ValueError as kesalahan:
    print("Konversi gagal:", type(kesalahan).__name__)