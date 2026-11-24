# continue melewatkan sisa blok pada putaran yang sedang berlangsung.
for angka in range(1, 6):
    if angka % 2 == 0:
        continue
    print("Ganjil:", angka)