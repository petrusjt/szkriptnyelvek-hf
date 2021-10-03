#!/usr/bin/env python3


def main():
    var_pairs = [("python", None), (0, True), (True, "alma"), (False, [])]
    for var1, var2 in var_pairs:
        print((bool(var1) or bool(var2)) and not (bool(var1) and bool(var2)))


if __name__ == "__main__":
    main()
