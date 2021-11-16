#!/usr/bin/env python3

from stack import Verem


class SorKetVeremmel:
    
    def __init__(self):
        self.verem1 = Verem()
        self.verem2 = Verem()

    def append(self, item):
        self.verem1.betesz(item)

    def popleft(self):
        while not self.verem1.ures():
            self.verem2.betesz(self.verem1.kivesz())
        
        value = self.verem2.kivesz()

        while not self.verem2.ures():
            self.verem1.betesz(self.verem2.kivesz())
        return value

    def is_empty(self):
        return self.verem1.meret() == 0

    def size(self):
        return self.verem1.meret()
    
    def __str__(self):
        return str(self.verem1)


def main():
    s = SorKetVeremmel()      # üres verem létrehozása
    print(s)         # [
    print(s.is_empty())  # True
    s.append(1)
    s.append(4)
    s.append(5)
    print(s)         # [1 4 5
    print(s.size()) # 3
    print(s.is_empty())  # False
    x = s.popleft()
    print(x)         # 1
    print(s)         # [4 5
    s.popleft()
    s.popleft()       # most már üres
    x = s.popleft()
    print(x)


if __name__ == "__main__":
    main()
