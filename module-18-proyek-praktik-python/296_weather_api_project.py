from unittest.mock import Mock

import requests


def cuaca(sesi, kota):
    respons = sesi.get("https://example.org/weather", params={"city": kota}, timeout=5)
    respons.raise_for_status()
    data = respons.json()
    return f"{kota}: {data['temperature']}°C"


if __name__ == "__main__":
    # Endpoint contoh bukan layanan cuaca nyata; mock memungkinkan demo offline.
    sesi = Mock(spec=requests.Session)
    sesi.get.return_value.json.return_value = {"temperature": 27}
    print(cuaca(sesi, "Bandung"))