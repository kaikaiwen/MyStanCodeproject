"""
File: caesar.py
Name: Kevin Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decrypt the password entered by the user.
    """
    print(caesar())


def caesar():
    """
    Using shifted ALPHABET to decrypt the password.
    """
    n = int(input('Secret Number: '))
    s = input("What\'s the ciphered string?")
    s = s.upper()
    new_alphabet = ''
    ans = ''
    for i in range(len(ALPHABET)):
        new_alphabet = ALPHABET[26-n:26]+ALPHABET[0:26-n]
    for i in range(len(s)):
        a = s[i]
        if s[i] == ' ':
            ans = ans+' '
        else:
            ans = ans + ALPHABET[new_alphabet.find(a)]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
