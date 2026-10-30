def angka_genap(data):
    for angka in data:
        if angka % 2 == 0:
            yield angka


def kuadrat(data):
    for angka in data:
        yield angka ** 2


# Pipeline meneruskan nilai antar-generator tanpa menyimpan daftar perantara.
print("Kuadrat genap:", list(kuadrat(angka_genap(range(1, 7)))))