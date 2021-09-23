#!/usr/bin/env python3

def palindrom(szoveg):
    i = 0
    while i < len(szoveg):
        if szoveg[i] != szoveg[-i - 1]:
            return False
        i += 1

    return True


def main():
    szoveg = input("Adj meg egy szöveget: ")
    print(palindrom(szoveg))


if __name__ == "__main__":
    main()

