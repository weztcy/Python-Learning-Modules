class Node:
    def __init__(self, nilai, berikutnya=None):
        self.nilai, self.berikutnya = nilai, berikutnya


# Node menyimpan nilai dan tautan; None menandai akhir list.
kepala = Node("A", Node("B", Node("C")))
sekarang = kepala
while sekarang is not None:
    print(sekarang.nilai)
    sekarang = sekarang.berikutnya