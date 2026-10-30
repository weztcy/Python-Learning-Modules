import json

# Contoh respons lokal memungkinkan parsing secara offline.
respons = '{"data": [{"nama": "Ayu", "nilai": 90}, {"nama": "Budi", "nilai": 80}]}'
data = json.loads(respons)
print("Nama pengguna:", [pengguna["nama"] for pengguna in data["data"]])