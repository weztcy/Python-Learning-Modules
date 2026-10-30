graf = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def jelajah(simpul, dikunjungi):
    if simpul in dikunjungi:
        return
    # DFS menyelesaikan satu cabang sebelum kembali ke pilihan lain.
    dikunjungi.add(simpul)
    print(simpul, end=" ")
    for tetangga in graf[simpul]:
        jelajah(tetangga, dikunjungi)


jelajah("A", set())
print()