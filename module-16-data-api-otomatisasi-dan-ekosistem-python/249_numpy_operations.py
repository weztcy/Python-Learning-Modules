import numpy as np

angka = np.array([1, 2, 3])
# Operasi pada ndarray berlaku per elemen tanpa loop Python eksplisit.
print("Dua kali:", angka * 2)
print("Rata-rata:", np.mean(angka))