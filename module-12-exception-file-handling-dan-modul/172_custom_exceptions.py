class SaldoTidakCukup(Exception):
    """Kesalahan khusus ketika penarikan melebihi saldo."""


def tarik(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoTidakCukup("Saldo tidak cukup")
    return saldo - jumlah


try:
    tarik(100, 150)
except SaldoTidakCukup as kesalahan:
    print(kesalahan)