class DaftarTugas:
    def __init__(self):
        self.tugas = []

    def tambah(self, judul):
        if not judul.strip():
            raise ValueError("Judul wajib diisi")
        self.tugas.append({"judul": judul, "selesai": False})

    def selesaikan(self, indeks):
        self.tugas[indeks]["selesai"] = True


if __name__ == "__main__":
    daftar = DaftarTugas()
    daftar.tambah("Belajar Python")
    daftar.selesaikan(0)
    print("Tugas:", daftar.tugas)