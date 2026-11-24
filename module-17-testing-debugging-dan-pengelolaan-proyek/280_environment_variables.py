import os

# getenv mengambil konfigurasi dari lingkungan tanpa menaruh rahasia di source code.
print("Mode aplikasi:", os.getenv("MODE_APLIKASI", "pengembangan"))