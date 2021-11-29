#!/usr/bin/env python3

import random


def shuffled(li):
    shuffled_li = li.copy()
    random.shuffle(shuffled_li)
    return shuffled_li


def main():
    li = list(range(10))
    shuffled_li = shuffled(li)

    print(f"Eredeti lista: {li}")
    print(f"Shuffled lista: {shuffled_li}")


if __name__ == "__main__":
    main()
