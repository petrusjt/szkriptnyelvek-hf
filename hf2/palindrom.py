#!/usr/bin/env python3


def is_palindrom(string):
    return string[::-1] == string


def main():
    text = input("Adj meg egy szöveget: ")
    print(is_palindrom(text))


if __name__ == "__main__":
    main()
