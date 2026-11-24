from bs4 import BeautifulSoup

# HTML lokal mendemonstrasikan scraper tanpa membebani situs lain.
html = '<ul><li class="produk">Buku</li><li class="produk">Pensil</li></ul>'
soup = BeautifulSoup(html, "html.parser")
print("Produk:", [item.get_text(strip=True) for item in soup.select(".produk")])