teks = "Kasur rusak"

# Hapus spasi dan samakan huruf agar hanya urutan huruf yang dibandingkan.
normal = "".join(karakter.lower() for karakter in teks if karakter.isalnum())
print("Teks:", teks)
print("Palindrom:", normal == normal[::-1])