#!/usr/bin/env python3


def is_palindrom(szam: int) -> bool:
    return str(szam) == str(szam)[::-1]


def is_prim(szam: int) -> bool:
    for i in range(2, szam):
        if szam % i == 0:
            return False

    return True


def prim_palindrom(n: int) -> int:
    m: int = n
    while not (is_prim(m) and is_palindrom(m)):
        m += 1

    return m


def main() -> None:
    print(f"prim_palindrom({31}) -> {prim_palindrom(31)}")
    print(f"prim_palindrom({130}) -> {prim_palindrom(130)}")
    print(f"prim_palindrom({131}) -> {prim_palindrom(131)}")
    print(f"prim_palindrom({1977}) -> {prim_palindrom(1977)}")


if __name__ == "__main__":
    main()
