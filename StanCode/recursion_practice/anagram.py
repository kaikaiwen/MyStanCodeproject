"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print('Welcome to stanCode \"Anagram Generator\"( or -1 to quit)')
    while True:
        anagram = input('Find_anagrams for:')
        if anagram == EXIT:
            break
        ans = find_anagrams(anagram)
        print(f"{len(ans)} anagrams: {ans}")
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    all_words = []
    with open(FILE, 'r')as f:
        for line in f:
            word = line.strip()
            all_words.append(word)
    return all_words


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dic = read_dictionary()
    anagrams = []
    find_anagrams_helper(s, s, [], dic, anagrams)
    return anagrams


def find_anagrams_helper(s, remain_s, current_lst, dictionary, anagrams):
    if len(current_lst) == len(s):
        word = ''.join(current_lst)
        if word in dictionary and word not in anagrams:
            print("Searching...")
            print("Found:", word)
            anagrams.append(word)
    else:
        for i in range(len(remain_s)):
            # choose
            current_lst.append(remain_s[i])
            # explore
            if has_prefix(''.join(current_lst)):
                new_remain_s = remain_s[:i] + remain_s[i + 1:]
                find_anagrams_helper(s, new_remain_s, current_lst, dictionary, anagrams)
            # un-choose
            current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    dic = read_dictionary()
    return has_prefix_helper(sub_s, dic)


def has_prefix_helper(sub_s, dic):
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
