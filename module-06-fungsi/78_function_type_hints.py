# Type hints menjelaskan tipe yang diharapkan, tetapi tidak dipaksakan Python.
def kali(angka: int, pengali: int) -> int:
    return angka * pengali


print("Hasil:", kali(4, 3))
print("Anotasi:", kali.__annotations__)