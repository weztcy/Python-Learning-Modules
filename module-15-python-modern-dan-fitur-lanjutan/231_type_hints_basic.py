# Type hints membantu pembaca dan alat statis; runtime tidak memaksanya.
def sapa(nama: str) -> str:
    return f"Halo, {nama}!"


print(sapa("Ayu"))