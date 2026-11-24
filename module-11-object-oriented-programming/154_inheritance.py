class Hewan:
    def bersuara(self):
        return "Suara hewan"


class Anjing(Hewan):
    pass


# Subclass mewarisi metode dari parent tanpa mendefinisikannya lagi.
print(Anjing().bersuara())