import sys

# prefix berbeda dari base_prefix ketika interpreter berjalan di dalam venv.
print("Dalam virtual environment:", sys.prefix != sys.base_prefix)
print("Buat environment: python -m venv .venv")