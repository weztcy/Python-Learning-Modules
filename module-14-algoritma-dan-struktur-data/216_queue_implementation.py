from collections import deque


class Antrian:
    def __init__(self):
        self.data = deque()

    def tambah(self, nilai):
        self.data.append(nilai)

    def layani(self):
        # popleft mengambil elemen yang pertama masuk (FIFO).
        return self.data.popleft()


antrian = Antrian()
antrian.tambah("Ayu")
antrian.tambah("Budi")
print(antrian.layani(), antrian.layani())