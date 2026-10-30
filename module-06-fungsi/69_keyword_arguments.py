def perkenalan(nama, kota):
    return f"{nama} tinggal di {kota}."


# Keyword arguments memasangkan nilai menurut nama, bukan posisinya.
print(perkenalan(kota="Bandung", nama="Ayu"))