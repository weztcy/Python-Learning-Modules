from functools import partial


def pangkat(basis, eksponen):
    return basis ** eksponen


# partial mengisi sebagian argumen sehingga pemanggil cukup memberi sisanya.
kuadrat = partial(pangkat, eksponen=2)
print("Kuadrat 5:", kuadrat(5))