def jelaskan(data):
    # Pola membongkar data sekaligus memilih cabang sesuai bentuk strukturnya.
    match data:
        case [x, y]:
            return f"Titik: {x}, {y}"
        case {"nama": nama}:
            return f"Nama: {nama}"
        case _:
            return "Tidak dikenal"


print(jelaskan([2, 3]))
print(jelaskan({"nama": "Ayu"}))