#!/usr/bin/env python3

ZERO = str(ord('a') - ord('a'))
ONE = str(ord('b') - ord('a'))
TWO = str(ord('c') - ord('a'))


def main():
    """Prints 2021 without using numbers in the source code."""
    
    print(TWO + ZERO + TWO + ONE)


if __name__ == "__main__":
    main()