def parse_angka(teks):
    try:
        return int(teks)
    except ValueError as kesalahan:
        # from menyimpan exception asal sebagai penyebab exception tingkat aplikasi.
        raise ValueError("Input harus angka") from kesalahan


try:
    parse_angka("x")
except ValueError as kesalahan:
    print("Pesan:", kesalahan)
    print("Penyebab:", type(kesalahan.__cause__).__name__)