def kuadrat(angka):
    return angka ** 2


# assert dipakai untuk memeriksa asumsi saat pengembangan, bukan validasi input pengguna.
assert kuadrat(3) == 9
assert kuadrat(0) == 0
print("Dua assertion berhasil")