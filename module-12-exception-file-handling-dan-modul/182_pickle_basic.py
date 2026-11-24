import pickle

data = {"nama": "Ayu", "skor": [80, 90]}
# Pickle hanya aman untuk data tepercaya; memuat pickle asing dapat menjalankan kode.
serial = pickle.dumps(data)
print("Dipulihkan:", pickle.loads(serial))