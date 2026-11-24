import hashlib

# SHA-256 menghasilkan digest tetap; hash bukan enkripsi yang bisa dibalik.
digest = hashlib.sha256("belajar".encode("utf-8")).hexdigest()
print("SHA-256:", digest)