from abc import ABC, abstractmethod


class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        """Setiap bentuk konkret harus mendefinisikan perhitungan luas."""


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2


# ABC tidak bisa dibuat langsung sebelum metode abstraknya diimplementasikan.
print("Luas:", Persegi(3).luas())