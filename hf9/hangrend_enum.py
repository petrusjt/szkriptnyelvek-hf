#!/usr/bin/env python3

from enum import Enum


class Hangrend(Enum):
    MELY = 1
    MAGAS = 2
    VEGYES = 3
    SEMMILYEN = 4


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def get_hangrend(word):
    van_mely_mgh = False
    van_magas_mgh = False

    for character in word:
        if character in MELY_MGHK:
            van_mely_mgh = True
        elif character in MAGAS_MGHK:
            van_magas_mgh = True

    if van_mely_mgh and van_magas_mgh:
        return Hangrend.VEGYES
    elif van_mely_mgh:
        return Hangrend.MELY
    elif van_magas_mgh:
        return Hangrend.MAGAS
    else:
        return Hangrend.SEMMILYEN


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for word in words:
        print("{}: {}".format(word, get_hangrend(word)))


if __name__ == "__main__":
    main()
