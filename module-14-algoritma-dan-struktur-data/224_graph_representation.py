# Adjacency list menyimpan tetangga tiap simpul; graf ini memiliki sisi dua arah.
graf = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
for simpul, tetangga in graf.items():
    print(simpul, "->", tetangga)