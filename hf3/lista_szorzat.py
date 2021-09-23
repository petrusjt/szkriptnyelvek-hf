#!/usr/bin/env python3

def lista_szorzat(lista):
    prod = 1
    for item in lista:
        prod *= item
    
    return prod


def main():
    lista = [1, 2, 3, 4, 5, 2]
    print(lista_szorzat(lista))


if __name__ == "__main__":
    main()

