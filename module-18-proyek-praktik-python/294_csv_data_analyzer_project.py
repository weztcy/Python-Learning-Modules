import csv
from io import StringIO


def rata_rata_csv(teks):
    baris = list(csv.DictReader(StringIO(teks)))
    if not baris:
        raise ValueError("Tidak ada baris data")
    return sum(float(item["nilai"]) for item in baris) / len(baris)


if __name__ == "__main__":
    # StringIO memungkinkan analisis format CSV tanpa file eksternal.
    print("Rata-rata:", rata_rata_csv("nama,nilai\nAyu,90\nBudi,80\n"))