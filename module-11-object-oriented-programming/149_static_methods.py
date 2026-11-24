class Matematika:
    @staticmethod
    def genap(angka):
        # Metode statis tidak membutuhkan self atau cls.
        return angka % 2 == 0


print("Genap:", Matematika.genap(8))