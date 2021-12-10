#!/usr/bin/env python3

import json

INPUT_FILENAME = "primes.json"


def is_palindrom(num):
    return str(num) == str(num)[::-1]


def main():
    with open(INPUT_FILENAME) as input_file:
        d = json.load(input_file)
    
    s = sum([prime for prime in d["data"] if is_palindrom(prime)])
    print(s)


if __name__ == "__main__":
    main()
