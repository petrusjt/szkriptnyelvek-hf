#!/usr/bin/env python3

EKEZETES_MGHK = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
EKEZET_NELKULI_MGHK = 'aeiooouuuAEIOOOUUU'


def ekezet_eltavolit(szoveg):
    ekezetmentes_szoveg = ""
    for karakter in szoveg:
        if karakter in EKEZETES_MGHK:
            index = EKEZETES_MGHK.find(karakter)
            ekezetmentes_karakter = EKEZET_NELKULI_MGHK[index]
        else:
            ekezetmentes_karakter = karakter
        ekezetmentes_szoveg += ekezetmentes_karakter

    return ekezetmentes_szoveg


def main():
    print(ekezet_eltavolit('áéíóöőúüűÁÉÍÓÖŐÚÜŰ'))


if __name__ == "__main__":
    main()
