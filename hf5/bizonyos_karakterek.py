#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Returns the characters of text that appear in chars as a string."""

    return "".join([character for character in text if character in chars])


def main():
    """Calls function valid with different parameters and prints result."""

    print("Barking!", valid("Barking!"), sep=" -> ")
    print("KL754", valid("KL754", chars="0123456789"), sep=" -> ")
    print("BEAN", valid("BEAN", chars="abcdefghijklmnopqrstuvwxyz"), sep=" -> ")


if __name__ == "__main__":
    main()
