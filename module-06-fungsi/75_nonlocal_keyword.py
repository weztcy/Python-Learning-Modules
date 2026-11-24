def buat_penghitung():
    jumlah = 0

    def tambah():
        # nonlocal mengubah variabel dari fungsi pembungkus, bukan variabel global.
        nonlocal jumlah
        jumlah += 1
        return jumlah

    return tambah


penghitung = buat_penghitung()
print(penghitung(), penghitung())