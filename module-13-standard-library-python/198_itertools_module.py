from itertools import combinations, islice

# combinations membuat pasangan tanpa pengulangan atau urutan terbalik.
print("Pasangan:", list(combinations("ABC", 2)))
print("Awal deret:", list(islice(range(100), 3)))