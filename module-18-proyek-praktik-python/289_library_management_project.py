class Perpustakaan:
    def __init__(self, judul):
        self.tersedia = set(judul)
        self.dipinjam = set()

    def pinjam(self, judul):
        if judul not in self.tersedia:
            raise ValueError("Buku tidak tersedia")
        self.tersedia.remove(judul)
        self.dipinjam.add(judul)

    def kembalikan(self, judul):
        if judul not in self.dipinjam:
            raise ValueError("Buku belum dipinjam")
        self.dipinjam.remove(judul)
        self.tersedia.add(judul)


if __name__ == "__main__":
    perpustakaan = Perpustakaan(["Python", "Algoritma"])
    perpustakaan.pinjam("Python")
    print("Dipinjam:", sorted(perpustakaan.dipinjam))
    perpustakaan.kembalikan("Python")
    print("Tersedia:", sorted(perpustakaan.tersedia))