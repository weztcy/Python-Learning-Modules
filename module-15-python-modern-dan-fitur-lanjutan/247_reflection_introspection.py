class Murid:
    def __init__(self, nama):
        self.nama = nama


murid = Murid("Ayu")
# getattr membaca atribut dari nama saat runtime; hasattr memeriksa keberadaannya.
print("Tipe:", type(murid).__name__)
print("Nama:", getattr(murid, "nama"))
print("Ada nilai:", hasattr(murid, "nilai"))