siswa = {"Ayu": {"kelas": "A", "nilai": 90}, "Budi": {"kelas": "B", "nilai": 82}}

# Akses kunci berlapis mengambil nilai dari dictionary bagian dalam.
print("Nilai Ayu:", siswa["Ayu"]["nilai"])
for nama, data in siswa.items():
    print(nama, "kelas", data["kelas"])