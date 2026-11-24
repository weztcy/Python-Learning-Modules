from contextlib import contextmanager


@contextmanager
def sesi():
    print("Buka")
    try:
        # yield membatasi blok with, finally menjamin penutupan.
        yield
    finally:
        print("Tutup")


with sesi():
    print("Proses")