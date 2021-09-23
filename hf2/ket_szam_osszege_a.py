#!/usr/bin/env python3


import sys


def main():
    if len(sys.argv) != 3:
        print("Mindkét számot meg kell adni!")
    else:
        print(int(sys.argv[1]) + int(sys.argv[2]))


if __name__ == "__main__":
    main()
