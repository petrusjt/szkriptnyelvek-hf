#!/usr/bin/env python3

import math


class Ellipse:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)


class Sphere:

    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4 * self.r * (math.pi ** 3)

    def surface_area(self):
        return 4 * math.pi * (self.r ** 2)

    def __lt__(self, other):
        return self.r < other.r

    def __le__(self, other):
        return self.r <= other.r

    def __gt__(self, other):
        return self. r > other.r

    def __ge__(self, other):
        return self.r >= other.r


def main():
    ellipse = Ellipse(1, 1)
    print(f"Area of 'ellipse': {ellipse.area()}")
    print(f"Perimeter of 'ellipse': {ellipse.perimeter()}")

    ellipse2 = Ellipse(4, 5)
    print(f"Area of 'ellipse2': {ellipse2.area()}")
    print(f"Perimeter of 'ellipse2': {ellipse2.perimeter()}")

    sphere = Sphere(1)
    print(f"Area of 'sphere': {sphere.volume()}")
    print(f"Perimeter of 'sphere': {sphere.surface_area()}")

    sphere2 = Sphere(4)
    print(f"Area of 'sphere2': {sphere2.volume()}")
    print(f"Perimeter of 'sphere2': {sphere2.surface_area()}")


if __name__ == "__main__":
    main()
