#!/usr/bin/env python3


def sztring_tisztit(string):
    tiszta_string = ""
    for character in string:
        if not character.isspace():
            tiszta_string += character

    return tiszta_string


def main():
    sztringek = ["192.20.246.138:\n 6666", "206.130.99.82:\n8080"]
    for sztring in sztringek:
        print(sztring_tisztit(sztring))


if __name__ == "__main__":
    main()
