#!/usr/bin/env python3

import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main():
    """Prints the english alphabet a-z or z-a based on the filename.
    
    If the filename is a-z.py, it prints the english alphabet a-z.
    If the filename is z-a.py, it prints the english alphabet z-a.
    Otherwise, the script does not output anything."""
    
    if sys.argv[0].endswith("a-z.py"):
        print(ALPHABET)
    elif sys.argv[0].endswith("z-a.py"):
        print(ALPHABET[::-1])


if __name__ == "__main__":
    main()
