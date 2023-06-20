"""
File: name_sq.py (extension)
Name: Kevin Chen
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    Making the text form a square.
    """
    name()


def name():
    """
    Arrange text , user input ,in a square.
    """
    print('This program prints a name in a square pattern!')
    n = input('Name: ')
    digit = len(n)
    for i in range(len(n)):
        for j in range(len(n)):
            if i == 0:
                print(n[j], end='')
            elif i == (digit-1):
                print(n[digit-1-j], end='')
            else:
                if j == 0:
                    print(n[i], end='')
                elif j == (digit-1):
                    print(n[digit-1-i], end='')
                else:
                    print(' ', end='')
        print('')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
