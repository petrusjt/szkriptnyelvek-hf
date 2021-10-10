#!/usr/bin/env python3

import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main():
    """Prints the english alphabet either from a-z or z-a based on the
    filename.
    
    If the script's filename is a-z.py, it prints the english 
    alphabet a-z.
    If the script's filename is z-a.py, it prints the english
    alphabet z-a.
    Otherwise, the script does not output anything."""
    
    if "a-z.py" in sys.argv[0]:
        print(ALPHABET)
    elif "z-a.py" in sys.argv[0]:
        print(ALPHABET[::-1])


if __name__ == "__main__":
    main()
