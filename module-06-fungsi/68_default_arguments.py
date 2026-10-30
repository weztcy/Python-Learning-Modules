# Nilai default dipakai jika pemanggil tidak memberikan argumen tersebut.
def sapa(nama="teman"):
    return f"Halo, {nama}!"


print(sapa())
print(sapa("Rani"))