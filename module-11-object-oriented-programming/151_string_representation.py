class Buku:
    def __init__(self, judul):
        self.judul = judul

    def __str__(self):
        return f"Buku: {self.judul}"

    def __repr__(self):
        # repr memprioritaskan representasi yang membantu debugging.
        return f"Buku({self.judul!r})"


buku = Buku("Python")
print(str(buku))
print(repr(buku))