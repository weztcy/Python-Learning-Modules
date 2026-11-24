nama = "global"


def contoh_scope():
    # Assignment lokal tidak mengubah variabel bernama sama di luar fungsi.
    nama = "lokal"
    print("Di dalam:", nama)


contoh_scope()
print("Di luar:", nama)