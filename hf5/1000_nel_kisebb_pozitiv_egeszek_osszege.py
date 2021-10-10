#!/usr/bin/env python3


def main():
    """Prints integers divisible by 3 or 5 or both under 1000."""
    
    print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))


if __name__ == "__main__":
    main()
