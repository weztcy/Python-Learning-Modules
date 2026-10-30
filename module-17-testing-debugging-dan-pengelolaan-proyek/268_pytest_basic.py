def perkalian(a, b):
    return a * b


def test_perkalian():
    # pytest menemukan test_ dan memperlakukan assert gagal sebagai test gagal.
    assert perkalian(3, 4) == 12


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-q", "-p", "no:cacheprovider"]))