def rata_rata(nilai):
    if not nilai:
        raise ValueError("Data kosong")
    return sum(nilai) / len(nilai)


# Kasus batas mencakup satu elemen serta input kosong yang harus ditolak.
assert rata_rata([5]) == 5
try:
    rata_rata([])
except ValueError as kesalahan:
    print("Kasus kosong:", kesalahan)