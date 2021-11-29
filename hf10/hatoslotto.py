#!/usr/bin/env python3

UPPER_LIMIT = 45 + 1


def main():
    for i in range(1, UPPER_LIMIT):
        for j in range(i + 1, UPPER_LIMIT):
            for k in range(j + 1, UPPER_LIMIT):
                for l in range(k + 1, UPPER_LIMIT):
                    for m in range(l + 1, UPPER_LIMIT):
                        for n in range(m + 1, UPPER_LIMIT):
                            if i + j + k + l + m + n == 90 and i * j * k * l * m * n == 996300:
                                print(i, j, k, l, m, n)


if __name__ == "__main__":
    main()
