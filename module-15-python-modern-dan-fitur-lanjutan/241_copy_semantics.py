import copy

asli = {"skor": [80]}
shallow = asli.copy()
deep = copy.deepcopy(asli)
# Salinan dangkal berbagi list dalam; salinan mendalam tidak.
asli["skor"].append(90)
print("Dangkal:", shallow["skor"])
print("Mendalam:", deep["skor"])