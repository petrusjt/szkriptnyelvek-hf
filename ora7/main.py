#!/usr/bin/env python3


def main():
    file = open("szoveg.txt", "r")
    for line in file:
        line = line.rstrip("\n")
        if line.endswith("."):
            print(line)
    file.close()


if __name__ == "__main__":
    main()
