from typing import get_type_hints


def tambah(a: int, b: int) -> int:
    return a + b


# get_type_hints membaca anotasi, tetapi tidak melakukan pemeriksaan tipe statis.
print("Anotasi:", get_type_hints(tambah))
print("Jalankan type checker terpisah untuk analisis statis sesungguhnya.")