#!/usr/bin/env python3


def main():
    """Finds and prints Münchausen numbers."""

    for i in range(440_000_000):
        s = 0
        num = i
        while num > 0:
            digit = num % 10
            num = num // 10
            if digit == 0:
                continue
            s += digit**digit

        if s == i:
            print(i)


if __name__ == "__main__":
    main()
