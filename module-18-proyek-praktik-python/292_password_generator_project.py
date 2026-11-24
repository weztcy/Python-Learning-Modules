import secrets
import string


def buat_panjang(panjang=16):
    if panjang < 8:
        raise ValueError("Panjang minimal 8 karakter")
    alfabet = string.ascii_letters + string.digits + string.punctuation
    # secrets cocok untuk kata sandi; panjang saja tidak menjamin kebijakan situs lain.
    return "".join(secrets.choice(alfabet) for _ in range(panjang))


if __name__ == "__main__":
    kata_sandi = buat_panjang()
    print("Kata sandi:", kata_sandi)
    print("Panjang:", len(kata_sandi))