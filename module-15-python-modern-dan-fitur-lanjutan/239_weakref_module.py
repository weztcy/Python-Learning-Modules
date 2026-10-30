import weakref


class Data:
    pass


objek = Data()
rujukan = weakref.ref(objek)
# Weak reference tidak mempertahankan objek ketika referensi kuat dihapus.
print("Sebelum:", rujukan() is objek)
del objek
print("Sesudah:", rujukan() is None)