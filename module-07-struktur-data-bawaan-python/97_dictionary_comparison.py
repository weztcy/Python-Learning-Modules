pertama = {"nama": "Ayu", "nilai": 80}
kedua = {"nilai": 80, "nama": "Ayu"}

# Kesamaan dictionary bergantung pada pasangan kunci-nilai, bukan urutan penulisannya.
print("Isi sama:", pertama == kedua)
kedua["nilai"] = 85
print("Setelah diubah:", pertama == kedua)