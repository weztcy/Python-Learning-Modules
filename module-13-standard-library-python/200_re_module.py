import re

teks = "Hubungi 081234567890 untuk informasi"
# \b membatasi kecocokan pada satu kata angka yang panjangnya 10–13 digit.
hasil = re.search(r"\b\d{10,13}\b", teks)
print("Nomor ditemukan:", hasil.group() if hasil else "tidak ada")