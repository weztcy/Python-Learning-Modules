def tampilkan(nilai: int | str) -> str:
    # Operator | pada anotasi menyatakan salah satu dari dua tipe.
    return str(nilai)


print(tampilkan(3), tampilkan("tiga"))