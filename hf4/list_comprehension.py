#!/usr/bin/env python3


def main():
    # 1. feladat
    print([word.upper() + "!" for word in ['auto', 'villamos', 'metro']])
    # 2. feladat
    print([word.capitalize() for word in ['aladar', 'bela', 'cecil']])
    # 3. feladat
    print([0 for _ in range(10)])
    # 4. feladat
    print([i * 2 for i in range(1, 11)])
    # 5. feladat
    print([int(num) for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
    # 6. feladat
    print([int(character) for character in "1234567"])
    # 7. feladat
    print([len(word) for word in 'The quick brown fox jumps over the lazy dog'.split()])
    # 8. feladat
    print([word[0] for word in "python is an awesome language".split()])
    # 9. feladat
    print([(word, len(word)) for word in 'The quick brown fox jumps over the lazy dog'.split()])
    # 10. feladat
    print([num for num in range(10) if num % 2 == 0])
    # 11. feladat
    print([num*num for num in range(20) if num*num % 2 == 0])
    # 12. feladat
    print([num*num for num in range(20) if str(num*num)[-1] == '4' ])
    # 13. feladat
    print(''.join([chr(character) for character in range(ord('A'), ord('Z') + 1)]))
    # 14. feladat
    print([word.strip() for word in [' apple ', ' banana ', ' kiwi']])
    # 15. feladat
    print(''.join([str(num) for num in [1, 0, 1, 1, 0, 1, 0, 0]]))


if __name__ == "__main__":
    main()

