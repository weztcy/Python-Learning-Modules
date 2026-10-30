import subprocess
import sys

# sys.executable memastikan proses anak memakai Python yang sama dengan induknya.
hasil = subprocess.run([sys.executable, "-c", "print(2 + 3)"], capture_output=True, text=True, check=True)
print("Keluaran proses anak:", hasil.stdout.strip())