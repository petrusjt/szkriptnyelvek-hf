#!/usr/bin/env python3

import random

KISBETUK = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
NAGYBETUK = KISBETUK.upper()
SZAMOK = "0123456789"
SPECIALIS_KARAKTEREK = ".,;_'*\""

KARAKTER_LISTA = [
    KISBETUK,
    NAGYBETUK,
    SZAMOK,
    SPECIALIS_KARAKTEREK
]


def get_password(length=8):
    if length < 8:
        raise ValueError

    password = []
    password.append(random.choice(KISBETUK))
    password.append(random.choice(NAGYBETUK))
    password.append(random.choice(SZAMOK))
    password.append(random.choice(SPECIALIS_KARAKTEREK))

    for _ in range(length - 4):
        password += random.choice(random.choice(KARAKTER_LISTA))
    
    random.shuffle(password)

    return "".join(password)


def main():
    pass


if __name__ == "__main__":
    main()
