class BisaBerenang:
    def berenang(self):
        return "Berenang"


class BisaTerbang:
    def terbang(self):
        return "Terbang"


# Pewarisan ganda menggabungkan perilaku dari dua parent independen.
class Bebek(BisaBerenang, BisaTerbang):
    pass


bebek = Bebek()
print(bebek.berenang(), bebek.terbang())