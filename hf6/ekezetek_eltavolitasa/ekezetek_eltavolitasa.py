#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
""".strip()

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
    print(ekezet_eltavolit(TEXT))


if __name__ == "__main__":
    main()
