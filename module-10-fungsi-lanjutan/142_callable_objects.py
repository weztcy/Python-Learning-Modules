class Pengali:
    def __init__(self, faktor):
        self.faktor = faktor

    def __call__(self, angka):
        # __call__ memungkinkan instance dipanggil seperti sebuah fungsi.
        return self.faktor * angka


tiga_kali = Pengali(3)
print("Hasil:", tiga_kali(4))