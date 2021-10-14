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
    pass


if __name__ == "__main__":
    main()
