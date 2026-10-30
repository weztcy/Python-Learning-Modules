import subprocess
import sys

# Menampilkan versi pip dengan interpreter aktif tanpa menginstal paket.
hasil = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True, check=True)
print(hasil.stdout.strip())
print("Instal paket lokal: python -m pip install -r requirements.txt")