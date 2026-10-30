PERTANYAAN = [("Berapa 2 + 3?", "5"), ("Bahasa pemrograman modul ini?", "python")]


def nilai(jawaban):
    # zip memasangkan jawaban dan kunci; jumlah respons harus tepat.
    if len(jawaban) != len(PERTANYAAN):
        raise ValueError("Jumlah jawaban tidak sesuai")
    return sum(teks.strip().lower() == kunci for teks, (_, kunci) in zip(jawaban, PERTANYAAN))


if __name__ == "__main__":
    print("Pertanyaan:", [teks for teks, _ in PERTANYAAN])
    print("Skor demo:", nilai(["5", "Python"]), "/", len(PERTANYAAN))