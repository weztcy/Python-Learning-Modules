from functools import wraps


def beri_label(fungsi):
    @wraps(fungsi)
    def pembungkus(*args, **kwargs):
        # Pembungkus menambah perilaku tanpa mengubah isi fungsi asli.
        return "Hasil: " + str(fungsi(*args, **kwargs))

    return pembungkus


@beri_label
def kuadrat(angka):
    return angka ** 2


print(kuadrat(4))