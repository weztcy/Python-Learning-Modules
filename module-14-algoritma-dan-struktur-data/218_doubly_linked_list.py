class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.sebelumnya = None
        self.berikutnya = None


# Tautan dua arah memungkinkan bergerak dari node pertama ke kedua dan kembali.
pertama, kedua = Node("A"), Node("B")
pertama.berikutnya = kedua
kedua.sebelumnya = pertama
print("Maju:", pertama.berikutnya.nilai)
print("Mundur:", kedua.sebelumnya.nilai)