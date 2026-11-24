import copy

asli = [[1], [2]]
dangkal = copy.copy(asli)
mendalam = copy.deepcopy(asli)
# Salinan dangkal masih berbagi list di dalam, deep copy menyalin hingga ke dalam.
asli[0].append(3)
print("Asli:", asli)
print("Dangkal:", dangkal)
print("Mendalam:", mendalam)