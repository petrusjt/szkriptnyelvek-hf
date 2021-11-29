#!/usr/bin/env python3

import csv
import re

FILENAME = "DT2.csv"
REGEX = r".*[jJ].*[sS].*[uU].*[nN].*"


def main():
    with open(FILENAME, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            if re.match(REGEX, row[0]):
                print(row[0])


if __name__ == "__main__":
    main()
