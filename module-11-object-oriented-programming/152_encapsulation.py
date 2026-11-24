class Rekening:
    def __init__(self, saldo):
        # Dua garis bawah memicu name mangling untuk mengurangi akses tak sengaja.
        self.__saldo = saldo

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah

    def lihat_saldo(self):
        return self.__saldo


rekening = Rekening(100)
rekening.tarik(30)
print("Saldo:", rekening.lihat_saldo())