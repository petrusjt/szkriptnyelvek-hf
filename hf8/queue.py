#!/usr/bin/env python3


class Sor:

    def __init__(self):
        self.inner_list = []

    def ures(self):
        return len(self.inner_list) == 0

    def meret(self):
        return len(self.inner_list)

    def betesz(self, ertek):
        self.inner_list.append(ertek)

    def kivesz(self):
        return self.inner_list.pop(0) if len(self.inner_list) > 0 else None

    def __str__(self):
        return "[" + " ".join([str(item) for item in self.inner_list])


def main():
    s = Sor()      # üres verem létrehozása
    print(s)         # [
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # [1 4 5
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # [4 5
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)


if __name__ == "__main__":
    main()
