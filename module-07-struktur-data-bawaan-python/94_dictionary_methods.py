murid = {"nama": "Budi", "nilai": 80}

# get memberi default saat kunci belum ada; pop menghapus serta mengembalikan nilai.
print("Kelas:", murid.get("kelas", "belum diisi"))
print("Nilai dihapus:", murid.pop("nilai"))
print("Sisa data:", murid)