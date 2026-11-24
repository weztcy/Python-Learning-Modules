class Positif:
    def __set_name__(self, pemilik, nama):
        self.nama = "_" + nama

    def __get__(self, instance, pemilik):
        if instance is None:
            return self
        return getattr(instance, self.nama)

    def __set__(self, instance, nilai):
        # Descriptor memvalidasi setiap assignment ke atribut yang dikelolanya.
        if nilai <= 0:
            raise ValueError("Nilai harus positif")
        setattr(instance, self.nama, nilai)


class Persegi:
    sisi = Positif()

    def __init__(self, sisi):
        self.sisi = sisi


print("Sisi:", Persegi(4).sisi)