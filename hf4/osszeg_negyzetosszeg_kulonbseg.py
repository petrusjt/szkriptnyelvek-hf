#!/usr/bin/env python3


def main():
    osszeg_negyzete = sum(range(1, 101)) ** 2
    negyzetosszeg = sum([num*num for num in range(1, 101)])
    print(osszeg_negyzete - negyzetosszeg)


if __name__ == "__main__":
    main()

