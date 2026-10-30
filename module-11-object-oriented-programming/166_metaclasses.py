class CatatNama(type):
    def __new__(mcls, nama, bases, namespace):
        # Metaclass menerima definisi class, lalu menambah atribut saat class dibuat.
        namespace["nama_class"] = nama
        return super().__new__(mcls, nama, bases, namespace)


class Produk(metaclass=CatatNama):
    pass


print("Nama class:", Produk.nama_class)