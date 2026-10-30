import textwrap

teks = "Satu kalimat panjang yang dapat dibungkus agar batas kolom dalam tampilan tetap mudah dibaca."
# textwrap memberi ilustrasi penataan teks; formatter kode tetap perlu alat khusus.
print(textwrap.fill(teks, width=40))