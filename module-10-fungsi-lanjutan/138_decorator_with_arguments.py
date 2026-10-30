from functools import wraps


def ulangi(jumlah):
    # Fungsi luar menangkap konfigurasi dekorator sebelum fungsi target diberikan.
    def dekorator(fungsi):
        @wraps(fungsi)
        def pembungkus(*args, **kwargs):
            for _ in range(jumlah):
                fungsi(*args, **kwargs)

        return pembungkus

    return dekorator


@ulangi(2)
def sapa(nama):
    print("Halo,", nama)


sapa("Ayu")