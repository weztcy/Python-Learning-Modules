class HitungMundur:
    def __init__(self, awal):
        self.sekarang = awal

    def __iter__(self):
        # Objek ini menyimpan sendiri posisi iterasinya.
        return self

    def __next__(self):
        if self.sekarang <= 0:
            raise StopIteration
        hasil = self.sekarang
        self.sekarang -= 1
        return hasil


for angka in HitungMundur(3):
    print(angka)