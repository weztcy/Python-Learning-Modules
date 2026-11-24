import logging
import sys

# Handler ke stdout membuat pesan log terlihat tanpa membuat file tambahan.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stdout)
logging.info("Proses dimulai")
logging.warning("Ini contoh peringatan")