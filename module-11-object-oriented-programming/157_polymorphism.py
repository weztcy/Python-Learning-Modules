class Kucing:
    def bersuara(self):
        return "Meong"


class Anjing:
    def bersuara(self):
        return "Guk"


# Kode pemanggil memakai antarmuka yang sama tanpa memeriksa class konkret.
for hewan in (Kucing(), Anjing()):
    print(hewan.bersuara())