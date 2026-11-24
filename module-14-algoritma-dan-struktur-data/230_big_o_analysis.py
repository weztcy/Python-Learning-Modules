def pencarian_linear(data, target):
    langkah = 0
    for nilai in data:
        langkah += 1
        if nilai == target:
            return langkah
    return langkah


# Kasus terburuk pencarian linear mengunjungi n elemen: O(n).
for panjang in (10, 100, 1000):
    print(f"n={panjang}, langkah={pencarian_linear(range(panjang), -1)}")