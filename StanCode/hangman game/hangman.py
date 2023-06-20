"""
File: hangman.py
Name: Kevin Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Guess what these letters are to reveal the hidden word.
    """
    hang_man()


def hang_man():
    """
    Input a letter ,if it  is in the word, then revealed from the blank letters.
    If wrong, try another letter.
    """
    ans = random_word()
    word = '_'*len(ans)
    print('The word look like '+word)
    print('You have ' + str(N_TURNS)+' wrong guesses left.')
    fail_count = 0
    while fail_count <= N_TURNS:
        if fail_count == N_TURNS:
            print('You are completely hung :(')
            print('The word was: ' + ans)
            break                                                               # No more life, stop the game.
        password = input_ch()
        if password in ans:
            print('You are correct!')
            word = replace(word, password, ans)
            if word == ans:
                print('You win!!')
                print('The word was: ' + ans)
                break                                                           # guess right, stop the game.
            else:
                print('The word look like ' + word)
        else:
            print('There is no ' + password.upper() + '\'s in the word')
            fail_count += 1
        print('You have ' + str(N_TURNS - fail_count) + ' wrong guesses left.')


def input_ch():
    """
    Input a letter and confirm whether it is in the correct format.
    """
    while True:
        p = input('Your Guess: ').upper()
        if (len(p) == 1) and p.isalpha():
            return p
            break
        else:
            print('illegal format.')


def replace(word, password, ans):
    """
    If letter is in the word, then revealed from the blank letters.
    """
    updated_word = ''
    for i in range(len(ans)):
        if password == ans[i]:
            updated_word += password
        else:
            updated_word += word[i]
    return updated_word


def random_word():
    """
    Importing the random word.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
