#!/usr/bin/env python3

INPUT = "szoveg.txt"
OUTPUT = "out.txt"


def main():
    f1 = open(INPUT, "r")
    to = open(OUTPUT, "w")

    for line in f1:
        to.write(line)

    f1.close()
    to.close()


    with open("string1.py", "r") as string1, open("string1_clean.py", "w") as string1_clean:
        for line in string1:
            if not line.strip().startswith('#'):
                string1_clean.write(line)


if __name__ == "__main__":
    main()
