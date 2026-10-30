import unittest


def tambah(a, b):
    return a + b


class TesTambah(unittest.TestCase):
    def test_positif(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_negatif(self):
        self.assertEqual(tambah(-2, 1), -1)


if __name__ == "__main__":
    # Runner mengembalikan exit code gagal jika salah satu test gagal.
    unittest.main(verbosity=2)