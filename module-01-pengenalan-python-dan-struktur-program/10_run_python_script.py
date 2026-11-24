import subprocess
import sys
from pathlib import Path

# __file__ memastikan path skrip contoh ditemukan tanpa bergantung pada lokasi terminal.
contoh = Path(__file__).with_name("01_hello_world.py")
print("Menjalankan:", contoh.name, flush=True)

# Gunakan interpreter yang sama untuk menjalankan file Python sebagai proses terpisah.
subprocess.run([sys.executable, str(contoh)], check=True)