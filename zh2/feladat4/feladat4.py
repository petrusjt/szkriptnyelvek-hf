#!/usr/bin/env python3

import sys
import password


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Adj meg egy számot!")
        elif len(sys.argv) > 2:
            raise ValueError("Egyetlen számot adj meg!")

        try:
            length = int(sys.argv[1])
        except ValueError:
            raise ValueError("Számot adj meg!")

        try:
            pw = password.get_password(length)
            print(pw)
        except ValueError:
            raise ValueError("A szám értéke legyen legalább 8!")
    except ValueError as e:
        print(e)
    

if __name__ == "__main__":
    main()
