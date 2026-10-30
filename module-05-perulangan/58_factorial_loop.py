n = 5
hasil = 1

# Faktorial n adalah hasil perkalian semua bilangan dari 1 sampai n.
for angka in range(1, n + 1):
    hasil *= angka
print(f"{n}! = {hasil}")