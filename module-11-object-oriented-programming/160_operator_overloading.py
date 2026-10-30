class Vektor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, lain):
        # + membuat vektor baru dengan menjumlahkan komponen seposisi.
        if not isinstance(lain, Vektor):
            return NotImplemented
        return Vektor(self.x + lain.x, self.y + lain.y)


hasil = Vektor(1, 2) + Vektor(3, 4)
print("Hasil:", hasil.x, hasil.y)