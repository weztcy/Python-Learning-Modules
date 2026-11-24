def terapkan(fungsi, data):
    # Fungsi dapat diberikan sebagai argumen seperti nilai lain.
    return [fungsi(nilai) for nilai in data]


def dua_kali(angka):
    return angka * 2


print("Hasil:", terapkan(dua_kali, [1, 2, 3]))