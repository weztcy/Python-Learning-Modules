class Titik:
    # __slots__ membatasi atribut instance ke nama yang didaftarkan.
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x, self.y = x, y


titik = Titik(2, 3)
print("Koordinat:", titik.x, titik.y)
print("Punya __dict__:", hasattr(titik, "__dict__"))