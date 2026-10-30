teks = ["apel", "pisang", "kiwi"]

# := menyimpan hasil ekspresi yang juga dipakai dalam kondisi yang sama.
for kata in teks:
    if (panjang := len(kata)) > 4:
        print(kata, "panjang:", panjang)