class Rekening:
    def __init__(self, saldo):
        self.saldo = saldo

    def setor(self, jumlah):
        # self merujuk ke rekening yang memanggil metode ini.
        self.saldo += jumlah


rekening = Rekening(100)
rekening.setor(50)
print("Saldo:", rekening.saldo)