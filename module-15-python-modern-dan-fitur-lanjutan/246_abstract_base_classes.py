from collections.abc import Iterable


class HitungMundur(Iterable):
    def __init__(self, awal):
        self.awal = awal

    def __iter__(self):
        # __iter__ memenuhi kontrak abstrak Iterable.
        return iter(range(self.awal, 0, -1))


print("Nilai:", list(HitungMundur(3)))