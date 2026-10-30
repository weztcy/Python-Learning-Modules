class TabelHash:
    def __init__(self, ukuran=5):
        self.bucket = [[] for _ in range(ukuran)]

    def simpan(self, kunci, nilai):
        # Tabrakan hash dikelola dengan menyimpan beberapa pasangan per bucket.
        kelompok = self.bucket[hash(kunci) % len(self.bucket)]
        for indeks, (lama, _) in enumerate(kelompok):
            if lama == kunci:
                kelompok[indeks] = (kunci, nilai)
                return
        kelompok.append((kunci, nilai))

    def ambil(self, kunci):
        for lama, nilai in self.bucket[hash(kunci) % len(self.bucket)]:
            if lama == kunci:
                return nilai
        raise KeyError(kunci)


tabel = TabelHash()
tabel.simpan("apel", 3)
print("Apel:", tabel.ambil("apel"))