#!/usr/bin/env python3


def diamond(height):
    if height % 2 == 0:
        print("The diamond's height can only be an odd value!")
        return
    
    for i in range(1, height, 2):
        print(('*'*i).center(height))
    
    for i in range(height, 0, -2):
        print(('*'*i).center(height))
        


def main():
    height = int(input('Height of the diamond: '))
    diamond(height)
    

if __name__ == "__main__":
    main()

