#!/usr/bin/env python3


def palindrom(szoveg):
    if len(szoveg) < 2:
        return True

    if szoveg[0] == szoveg[-1]:
        return palindrom(szoveg[1:-1])
    else:
        return False


def main():
    szoveg = input("Adj meg egy szöveget: ")
    print(palindrom(szoveg))


if __name__ == "__main__":
    main()

