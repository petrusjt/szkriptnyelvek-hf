#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""".strip()


def main():
    for character in TEXT:
        if character.isalpha():
            if character.isupper():
                print(chr((ord(character) + 2 - 65) % 26 + 65), end='')
            else:
                print(chr((ord(character) + 2 - 97) % 26 + 97), end='')
        else:
            print(character, end='')
    print()


if __name__ == "__main__":
    main()

