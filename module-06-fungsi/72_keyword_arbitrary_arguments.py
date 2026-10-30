# **kwargs menampung argumen bernama dalam dictionary.
def tampilkan_data(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")


tampilkan_data(nama="Sari", usia=22)