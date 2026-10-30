class Penanda:
    def __enter__(self):
        print("Mulai")
        return self

    def __exit__(self, tipe, nilai, traceback):
        # False tidak menyembunyikan exception dalam blok with.
        print("Selesai")
        return False


with Penanda():
    print("Bekerja")