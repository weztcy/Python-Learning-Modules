class Mesin:
    def hidupkan(self):
        return "Mesin hidup"


class Mobil:
    def __init__(self):
        # Mobil memiliki Mesin, bukan merupakan subclass dari Mesin.
        self.mesin = Mesin()


print(Mobil().mesin.hidupkan())