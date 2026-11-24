from bs4 import BeautifulSoup


def judul_artikel(html):
    soup = BeautifulSoup(html, "html.parser")
    return [item.get_text(strip=True) for item in soup.select("article h2")]


if __name__ == "__main__":
    # Scraping HTML lokal tidak memerlukan izin atau koneksi ke situs eksternal.
    contoh = "<article><h2>Belajar Python</h2></article><article><h2>Proyek Data</h2></article>"
    print("Artikel:", judul_artikel(contoh))