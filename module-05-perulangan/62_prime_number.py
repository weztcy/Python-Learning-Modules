angka = 29

# Cukup uji pembagi sampai akar kuadrat; faktor yang lebih besar berpasangan dengan yang kecil.
if angka < 2:
    prima = False
else:
    prima = True
    for pembagi in range(2, int(angka ** 0.5) + 1):
        if angka % pembagi == 0:
            prima = False
            break
print(angka, "prima" if prima else "bukan prima")