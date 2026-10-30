class Node:
    def __init__(self, nilai):
        self.nilai, self.kiri, self.kanan = nilai, None, None


def sisip(akar, nilai):
    if akar is None:
        return Node(nilai)
    # Nilai kecil ke kiri, nilai besar ke kanan; duplikat diabaikan.
    if nilai < akar.nilai:
        akar.kiri = sisip(akar.kiri, nilai)
    elif nilai > akar.nilai:
        akar.kanan = sisip(akar.kanan, nilai)
    return akar


akar = None
for nilai in (5, 3, 7):
    akar = sisip(akar, nilai)
print("Akar dan anak:", akar.nilai, akar.kiri.nilai, akar.kanan.nilai)