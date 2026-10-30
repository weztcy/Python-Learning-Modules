class Dasar:
    def sapa(self):
        return "Dasar"


class Kiri(Dasar):
    def sapa(self):
        return "Kiri"


class Kanan(Dasar):
    def sapa(self):
        return "Kanan"


class Gabungan(Kiri, Kanan):
    pass


# MRO menentukan cabang mana yang diperiksa pertama pada diamond inheritance.
print("Metode:", Gabungan().sapa())
print("Urutan:", [kelas.__name__ for kelas in Gabungan.__mro__])