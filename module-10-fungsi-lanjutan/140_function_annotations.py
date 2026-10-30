def luas(panjang: float, lebar: float) -> float:
    return panjang * lebar


# Anotasi disimpan sebagai metadata, bukan pemeriksaan tipe otomatis.
print("Luas:", luas(2.5, 4.0))
print("Anotasi:", luas.__annotations__)