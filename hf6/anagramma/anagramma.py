#!/usr/bin/env python3


def normalize(string : str):
    s = string.lower()
    res = ""
    for c in s:
        if not c.isspace():
            res += c

    return res



def is_anagramma1(szo1, szo2):
    return sorted(normalize(szo1)) == sorted(normalize(szo2))


def is_anagramma2(szo1, szo2):
    s1 = normalize(szo1)
    s2 = normalize(szo2)
    for karakter in s1:
        if karakter not in s2:
            return False
    
    return True


def main():
    pass


if __name__ == "__main__":
    main()

