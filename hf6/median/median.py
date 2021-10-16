#!/usr/bin/env python3


def get_median(li):
    lista = sorted(li)
    if len(lista) % 2 == 0:
        return lista[len(lista) // 2]
    else:
        m_1 = lista[len(lista) // 2]
        m_2 = lista[len(lista) // 2 + 1]
        return (m_1 + m_2) / 2


def main():
    adatok = [
        [1, 2, 3, 4, 5], [3, 1, 2, 5, 3],
        [1, 300, 2, 200, 1], [3, 6, 20, 99, 10, 15]
    ]
    for adat in adatok:
        print(f"{adat} -> {get_median(adat)}")


if __name__ == "__main__":
    main()
