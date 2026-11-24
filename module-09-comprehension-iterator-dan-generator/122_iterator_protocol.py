class AngkaGenap:
    def __init__(self, batas):
        self.batas = batas

    def __iter__(self):
        # Kembalikan iterator baru supaya tiap perulangan dimulai dari awal.
        return iter(range(2, self.batas + 1, 2))


data = AngkaGenap(6)
print("Pertama:", list(data))
print("Kedua:", list(data))