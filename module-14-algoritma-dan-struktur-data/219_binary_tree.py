class Node:
    def __init__(self, nilai, kiri=None, kanan=None):
        self.nilai, self.kiri, self.kanan = nilai, kiri, kanan


# Setiap node dapat memiliki paling banyak dua anak.
akar = Node("A", Node("B"), Node("C"))
print("Akar:", akar.nilai, "Anak:", akar.kiri.nilai, akar.kanan.nilai)