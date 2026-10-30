def jumlah_bersarang(data):
    total = 0
    for elemen in data:
        # Rekursi menjelajahi list bersarang yang kedalamannya tidak diketahui.
        if isinstance(elemen, list):
            total += jumlah_bersarang(elemen)
        else:
            total += elemen
    return total


print("Jumlah:", jumlah_bersarang([1, [2, 3], [4, [5]]]))