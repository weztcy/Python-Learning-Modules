import requests

# Siapkan request tanpa jaringan untuk memeriksa metode dan URL hasilnya.
permintaan = requests.Request("GET", "https://example.org/api", params={"halaman": 1}).prepare()
print("Metode:", permintaan.method)
print("URL:", permintaan.url)