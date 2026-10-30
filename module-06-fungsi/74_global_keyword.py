jumlah_panggilan = 0


def tambah_panggilan():
    # global memungkinkan assignment ke nama pada lingkup modul.
    global jumlah_panggilan
    jumlah_panggilan += 1


tambah_panggilan()
tambah_panggilan()
print("Jumlah panggilan:", jumlah_panggilan)