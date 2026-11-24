from typing import cast

nilai: object = "Python"
# cast membantu pemeriksa statis, tetapi tidak mengonversi objek saat runtime.
teks = cast(str, nilai)
print("Huruf besar:", teks.upper())
print("Objek sama:", teks is nilai)