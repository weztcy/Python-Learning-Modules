import random

# Batas percobaan membuat permainan pasti selesai meskipun tebakan salah.
rahasia = random.randint(1, 10)
print("Tebak bilangan 1-10 (maksimal 3 percobaan).")
for kesempatan in range(3):
    try:
        tebakan = int(input(f"Percobaan {kesempatan + 1}: "))
    except ValueError:
        print("Masukkan bilangan bulat.")
        continue
    if tebakan == rahasia:
        print("Tepat!")
        break
    print("Terlalu kecil" if tebakan < rahasia else "Terlalu besar")
else:
    print("Kesempatan habis. Jawaban:", rahasia)