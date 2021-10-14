#!/usr/bin/env python3


def get_szamjegyek_osszege(szam):
    return sum([int(szamjegy) for szamjegy in str(szam)])


def main():
    print(get_szamjegyek_osszege(2 ** 1000))


if __name__ == "__main__":
    main()
