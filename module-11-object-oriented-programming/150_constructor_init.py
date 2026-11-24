class Persegi:
    def __init__(self, sisi):
        # __init__ menginisialisasi instance baru sebelum digunakan.
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2


print("Luas:", Persegi(4).luas())