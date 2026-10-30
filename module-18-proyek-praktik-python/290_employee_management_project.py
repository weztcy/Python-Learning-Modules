class Perusahaan:
    def __init__(self):
        self.pegawai = {}

    def tambah(self, nomor, nama, gaji):
        if nomor in self.pegawai or gaji < 0:
            raise ValueError("Nomor sudah ada atau gaji negatif")
        self.pegawai[nomor] = {"nama": nama, "gaji": gaji}


if __name__ == "__main__":
    perusahaan = Perusahaan()
    perusahaan.tambah(1, "Ayu", 5000000)
    print("Pegawai:", perusahaan.pegawai)