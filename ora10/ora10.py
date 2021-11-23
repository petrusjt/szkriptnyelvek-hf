#!/usr/bin/env python3

import random
from typing import List


def shuffled(li: List[int]) -> List[int]:
    l = li.copy()
    random.shuffle(l)
    return l


def main() -> None:
    li = list(range(10))
    l = shuffled(li)
    print(li)
    print(l)


if __name__ == "__main__":
    main()
