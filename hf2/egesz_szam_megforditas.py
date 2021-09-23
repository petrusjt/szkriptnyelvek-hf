#!/usr/bin/env python3


def egesz_szam_megfordit(szam):
    return int(str(szam)[::-1])


def main():
    szam = int(input("Adj meg egy egész számot: "))
    print(egesz_szam_megfordit(szam))


if __name__ == "__main__":
    main()
