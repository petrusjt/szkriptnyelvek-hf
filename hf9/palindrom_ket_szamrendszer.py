#!/usr/bin/env python3

from typing import List


def decimal_to_binary(num: int) -> str:
    return bin(num)[2:]


def is_palindrom(string: str) -> bool:
    return string == string[::-1]


def main() -> None:
    s: int = 0
    for i in range(1000000):
        if is_palindrom(str(i)) and is_palindrom(decimal_to_binary(i)):
            s += i
    print(s)


if __name__ == "__main__":
    main()
