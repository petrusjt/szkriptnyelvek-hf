from szamjegyek_osszege import get_szamjegyek_osszege


def test_get_szamjegyek_osszege():
    assert 1366 == get_szamjegyek_osszege(2 ** 1000)
    assert 10 == get_szamjegyek_osszege(19)
    assert 3 == get_szamjegyek_osszege(30)
    assert 33 == get_szamjegyek_osszege(23532441414)