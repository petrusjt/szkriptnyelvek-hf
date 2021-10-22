#!/usr/bin/env python3


def main():
    with open("szamok.txt", "r") as szamok:
        print(str(sum([int(line) for line in szamok]))[:10])


if __name__ == "__main__":
    main()
