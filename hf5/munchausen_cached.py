#!/usr/bin/env python3

EXPONENTIATION_CACHE = [0] + [num ** num for num in range(1, 10)]
CACHE = {}


def is_munchausen(number):
    sorted_digits = "".join(sorted(str(number))).replace('0', '')

    if sorted_digits not in CACHE.keys():
        s = 0
        num = number
        while num > 0:
            digit = num % 10
            num = num // 10
            s += EXPONENTIATION_CACHE[digit]
        CACHE[sorted_digits] = s
    
    return CACHE[sorted_digits] == number


def main():
    for i in range(440_000_000):
        if is_munchausen(i):
            print(i)


if __name__ == "__main__":
    main()
