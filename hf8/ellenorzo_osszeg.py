#!/usr/bin/env python3


def get_checksum(l):
    return sum([max(line) - min(line) for line in l])


def main():
    with open("input.txt", "r") as file:
        lines = [[int(item) for item in line.rstrip("\n").split()] for line in file]
        print(get_checksum(lines))


if __name__ == "__main__":
    main()
