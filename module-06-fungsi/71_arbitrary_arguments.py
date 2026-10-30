# *args menampung sejumlah argumen posisi dalam sebuah tuple.
def jumlahkan(*angka):
    return sum(angka)


print("Total:", jumlahkan(2, 3, 5))