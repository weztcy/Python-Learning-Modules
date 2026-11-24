import platform
import sys

# sys.executable menunjukkan lokasi interpreter yang sedang menjalankan file ini.
print("Implementasi:", platform.python_implementation())
print("Versi:", platform.python_version())
print("Interpreter:", sys.executable)