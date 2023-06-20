"""
File: complement.py
Name: Kevin Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Finding the complement strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    Find complementary DNA sequence after checking for non-empty strings.
    """
    if dna == '':
        return 'DNA strand is missing.'
    else:
        ans = ''
        for i in range(len(dna)):
            alphabet = dna[i]
            if alphabet == 'A':
                ans = ans+'T'
            elif alphabet == 'T':
                ans = ans+'A'
            elif alphabet == 'C':
                ans = ans+'G'
            else:
                ans = ans + 'C'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
