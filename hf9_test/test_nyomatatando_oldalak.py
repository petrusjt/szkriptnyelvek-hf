import sys
sys.path.append("c:\\dev\\git\\szkriptnyelvek-hf")

from hf9.nyomtatando_oldalak import nyomtatando_oldalak


def test_01_get_nyomtatando_oldalak():
    assert nyomtatando_oldalak("1,4,5") == [1, 4, 5]


def test_02_get_nyomtatando_oldalak():
    assert nyomtatando_oldalak("1-5") == [1, 2, 3, 4, 5]


def test_03_get_nyomtatando_oldalak():
    assert nyomtatando_oldalak("1,3-5,7") == [1, 3, 4, 5, 7]


def test_04_get_nyomtatando_oldalak():
    assert nyomtatando_oldalak("1,3-5,7,11-13") == [1, 3, 4, 5, 7, 11, 12, 13]
