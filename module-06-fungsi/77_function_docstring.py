def luas_persegi_panjang(panjang, lebar):
    """Hitung luas persegi panjang dari dua panjang sisi positif."""
    return panjang * lebar


# __doc__ memungkinkan penjelasan fungsi dibaca saat runtime.
print("Dokumentasi:", luas_persegi_panjang.__doc__)
print("Luas:", luas_persegi_panjang(4, 3))