#!/usr/bin/env python3


def normalize(string):
    res = ""
    for c in string.lower():
        if not c.isspace():
            res += c

    return res


def is_anagramma1(szo1, szo2):
    return sorted(normalize(szo1)) == sorted(normalize(szo2))


def is_anagramma2(szo1, szo2):
    s1 = normalize(szo1)
    s2 = normalize(szo2)
    if len(s1) != len(s2):
        return False

    for karakter in s1:
        if karakter not in s2:
            return False
    
    return True


def get_charmap(szo):
    d = {}
    for karakter in szo:
        if karakter not in d:
            d[karakter] = 1
        else:
            d[karakter] += 1

    return d


def is_anagramma3(szo1, szo2):
    s1_charmap = get_charmap(normalize(szo1))
    s2_charmap = get_charmap(normalize(szo2))
    
    return s1_charmap == s2_charmap


def main():
    adatok = [
        ('listen', 'silent'), ('A gentleman', 'Elegant man'),
        ('Clint Eastwood', 'Old west action'), ('dormitory', 'dirty room'),
        ('alma', 'körte'), ('óra', 'apró')
    ]

    print('is_anagramma1')
    for adat in adatok:
        print(f"{adat[0]}, {adat[1]} -> {is_anagramma1(adat[0], adat[1])}")

    print('\nis_anagramma2')
    for adat in adatok:
        print(f"{adat[0]}, {adat[1]} -> {is_anagramma2(adat[0], adat[1])}")

    print('\nis_anagramma3')
    for adat in adatok:
        print(f"{adat[0]}, {adat[1]} -> {is_anagramma3(adat[0], adat[1])}")


if __name__ == "__main__":
    main()

