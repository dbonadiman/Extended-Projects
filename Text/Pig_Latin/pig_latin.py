"""
Problem
-------
**Pig Latin**
Pig Latin is a game of alterations played
on the English language game. To create the
Pig Latin form of an English word the initial
consonant sound is transposed to the end of the
word and an ay is affixed (Ex.: "banana" would
yield anana-bay). Read Wikipedia for more
information on rules.


Solution
--------
The solution is done doing a list split and then a string
join with some pig latins added ;)


Author
------
dbonadiman

"""
import sys


def pig_latin(s):
    """
    pig_latin
    It uses the string join function
    to create a list

    Parameter:
    s ==> the string to piggify

    Test:
    >>> pig_latin('ciao')
    'iao-cay'

    >>> pig_latin('banana')
    'anana-bay'
    """
    return "".join([s[1:], "-", s[0], "ay"])


def main():
    try:
        print("\nThis program piggify a string\n"
              "More in detail it takes your string and makes and\n"
              "Translate it in pig latin removing the first letter and\n"
              "adding it to the end folowed by ay.\n"
              "Please enter the string you want to convert.\n")

        string = raw_input("--> ")
        print(pig_latin(string))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
