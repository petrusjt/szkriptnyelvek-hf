#!/usr/bin/env python3

from typing import List


def nyomtatando_oldalak(megadott_oldalak: str) -> List[int]:
    oldalak: List[int] = []
    for oldal in megadott_oldalak.split(','):
        if "-" in oldal:
            minimum, maximum = oldal.split("-")
            oldalak += range(int(minimum), int(maximum) + 1)
        else:
            oldalak.append(int(oldal))
    
    return oldalak


def main() -> None:
    inp = "1-4,7,9,11-15"
    print(f"{inp}: {nyomtatando_oldalak(inp)}")


if __name__ == "__main__":
    main()
