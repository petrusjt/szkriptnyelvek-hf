#!/usr/bin/env python3


def myfunc1(item):
    return item[3]


def feladat_1():
    data = [ 
        (1, 'Albany', 'NY', 162692),
        (3, 'Allegany', 'NY', 11986),
        (121, 'Wyoming', 'NY', 8722),
        (123, 'Yates', 'NY', 5094)
    ]
    print(sorted(data, key=myfunc1))
    print(sorted(data, key=lambda item: item[3]))


def myfunc2(user):
    return int(user.split(':')[0])


def feladat_2():
    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(lst, reverse=True, key=myfunc2))
    print(sorted(lst, reverse=True, key=lambda item: int(item.split(':')[0])))


def myfunc3(row):
    return row[1]


def feladat_3():
    li = [[2, 6], [1, 3], [5, 4]]
    print(sorted(li, key=myfunc3))
    print(sorted(li, key=lambda row: row[1]))


def main():
    feladat_1()
    feladat_2()
    feladat_3()


if __name__ == "__main__":
    main()
