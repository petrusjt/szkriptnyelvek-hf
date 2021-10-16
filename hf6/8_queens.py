#!/usr/bin/env python3

def print_queens(queens):
    print("+-----------------+")
    for i in range(8):
        print("|", end='')
        for j in range(8):
            if 7 - queens[j] == i:
                print(" Q", end='')
            else:
                print(" .", end='')
        print(" |")
    print("+-----------------+")


def main():
    print_queens([7,3,0,2,5,1,6,4])
    pass


if __name__ == "__main__":
    main()
