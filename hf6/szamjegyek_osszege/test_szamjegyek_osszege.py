from szamjegyek_osszege import get_szamjegyek_osszege


def test_get_szamjegyek_osszege():
    assert get_szamjegyek_osszege(2 ** 1000) == 1366
    assert get_szamjegyek_osszege(19) == 10
    assert get_szamjegyek_osszege(30) == 3
    assert get_szamjegyek_osszege(23532441414) == 33
