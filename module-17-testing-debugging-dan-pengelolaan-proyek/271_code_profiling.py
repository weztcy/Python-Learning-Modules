import cProfile
import io
import pstats


def pekerjaan():
    return sum(angka * angka for angka in range(1000))


# Profil mencatat banyak pemanggilan dan waktu setiap fungsi.
profil = cProfile.Profile()
hasil = profil.runcall(pekerjaan)
buffer = io.StringIO()
pstats.Stats(profil, stream=buffer).sort_stats("cumulative").print_stats(5)
print("Hasil:", hasil)
print(buffer.getvalue())