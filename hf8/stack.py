#!/usr/bin/env python3

class Verem:

    def __init__(self):
        self.inner_list = []

    def ures(self):
        return len(self.inner_list) == 0

    def meret(self):
        return len(self.inner_list)

    def betesz(self, ertek):
        self.inner_list.append(ertek)

    def kivesz(self):
        return self.inner_list.pop() if len(self.inner_list) > 0 else None

    def __str__(self):
        return "[" + " ".join([str(item) for item in self.inner_list])


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

if __name__ == "__main__":
    main()