class Murid:
    def __init__(self, nama):
        # Setiap instance memiliki atribut nama masing-masing.
        self.nama = nama


print(Murid("Ayu").nama, Murid("Budi").nama)