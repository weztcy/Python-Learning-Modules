# compile memeriksa sintaks string kode tanpa menjalankannya.
# Contoh salah disimpan sebagai string agar file pembelajaran tetap valid.
contoh_salah = "if True print('Halo')"
try:
    compile(contoh_salah, "contoh_salah.py", "exec")
except SyntaxError as kesalahan:
    print("Kesalahan sintaks:", kesalahan.msg)

# Versi benar memakai titik dua sebelum blok if yang diindentasi.
contoh_benar = "if True:\n    print('Halo')"
exec(compile(contoh_benar, "contoh_benar.py", "exec"))