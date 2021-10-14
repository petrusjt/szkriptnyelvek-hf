#!/usr/bin/env python3

CONST = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 'ú': 'u',
    'ü': 'u', 'ű': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ö': 'O',
    'Ő': 'O', 'Ú': 'U', 'Ü': 'U', 'Ű': 'U'
}


def ekezet_eltavolit(szoveg):
    karaktermentes_szoveg = szoveg
    for ekezetes_karakter, ekezetmentes_karakter in CONST.items():
        karaktermentes_szoveg = karaktermentes_szoveg.replace(ekezetes_karakter, 
            ekezetmentes_karakter)

    return karaktermentes_szoveg

def main():
    print(ekezet_eltavolit('áéíóöőúüűÁÉÍÓÖŐÚÜŰ'))


if __name__ == "__main__":
    main()
