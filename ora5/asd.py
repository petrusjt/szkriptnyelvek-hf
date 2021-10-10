#!/usr/bin/env python3


def loop(limit, debug=False):
    if debug:
        print("ciklus kezdete")

    for i in range(1, limit+1):
        print(i, end=" ")
    
    if debug:
        print("\nciklus vége", end=" ")
    print()


def main():
    loop(10)
    loop(10, debug=True)


if __name__ == "__main__":
    main()
