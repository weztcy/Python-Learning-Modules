from collections import deque

graf = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
antrian = deque(["A"])
dikunjungi = {"A"}
urutan = []
# Antrian FIFO memastikan BFS mengunjungi simpul per tingkat.
while antrian:
    simpul = antrian.popleft()
    urutan.append(simpul)
    for tetangga in graf[simpul]:
        if tetangga not in dikunjungi:
            dikunjungi.add(tetangga)
            antrian.append(tetangga)
print("BFS:", urutan)