#!/usr/bin/env python3


def main():
    print(sum([sum([int(szamjegy) for szamjegy in list(str(num))]) for num in range(1, 101)]))


if __name__ == "__main__":
    main()
