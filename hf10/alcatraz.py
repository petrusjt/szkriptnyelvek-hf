#!/usr/bin/env python3

CELLAK_SZAMA = 600


def main():
    cellak = [False] * CELLAK_SZAMA
    for i in range(0, CELLAK_SZAMA):
        for j in range(i, CELLAK_SZAMA, i + 1):
            cellak[j] = not cellak[j]

    nyitott_cellak = [str(idx + 1) for idx, item in enumerate(cellak) if item]
    print(", ".join(nyitott_cellak))


if __name__ == "__main__":
    main()
