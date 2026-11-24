from functools import wraps


def tambah_satu(fungsi):
    @wraps(fungsi)
    def pembungkus(angka):
        return fungsi(angka) + 1

    return pembungkus


def dua_kali(fungsi):
    @wraps(fungsi)
    def pembungkus(angka):
        return fungsi(angka) * 2

    return pembungkus


# Dekorator yang paling dekat dengan def diterapkan lebih dulu.
@dua_kali
@tambah_satu
def nilai(angka):
    return angka


print("Hasil (3+1)*2:", nilai(3))