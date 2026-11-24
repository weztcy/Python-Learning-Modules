from pathlib import Path
from tempfile import TemporaryDirectory


def rapikan(folder):
    dipindahkan = []
    for berkas in folder.iterdir():
        if berkas.is_file():
            tujuan = folder / (berkas.suffix.lower().lstrip(".") or "tanpa_ekstensi")
            tujuan.mkdir(exist_ok=True)
            berkas.rename(tujuan / berkas.name)
            dipindahkan.append((berkas.name, tujuan.name))
    return dipindahkan


if __name__ == "__main__":
    # Berkas demo berada dalam folder sementara agar berkas pengguna tidak dipindah.
    with TemporaryDirectory() as sementara:
        folder = Path(sementara)
        (folder / "catatan.txt").write_text("Belajar", encoding="utf-8")
        (folder / "nilai.csv").write_text("nama,nilai\n", encoding="utf-8")
        print("Dipindahkan:", rapikan(folder))