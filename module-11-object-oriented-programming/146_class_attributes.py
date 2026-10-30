class Lingkaran:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius


# pi dibagi pada tingkat class; radius dimiliki masing-masing instance.
print("Luas:", Lingkaran.pi * Lingkaran(2).radius ** 2)