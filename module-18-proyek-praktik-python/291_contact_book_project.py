class Kontak:
    def __init__(self):
        self.data = {}

    def simpan(self, nama, nomor):
        if not nama.strip() or not nomor.strip():
            raise ValueError("Nama dan nomor wajib diisi")
        self.data[nama] = nomor

    def cari(self, nama):
        return self.data.get(nama, "Tidak ditemukan")


if __name__ == "__main__":
    buku = Kontak()
    buku.simpan("Ayu", "081234567890")
    print("Ayu:", buku.cari("Ayu"))