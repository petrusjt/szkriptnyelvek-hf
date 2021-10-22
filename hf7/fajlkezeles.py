#!/usr/bin/env python3

STRING1 = "string1.py"
STRING1_CLEAN = "string1_clean.py"


def main():
    with open(STRING1, "r") as string1_file, open(STRING1_CLEAN, "w") as string1_clean_file:
        for line in string1_file:
            line = line.rstrip("\n")
            if not line.lstrip().startswith("#"):
                print(line, file=string1_clean_file)


if __name__ == "__main__":
    main()
