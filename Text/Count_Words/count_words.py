

"""
Problem
-------
**Count Words in a String**
Counts the number of individual words in a string.
For added complexity read these strings in from a
text file and generate a summary.


Solution
--------
The solution is provided using a simple string split

Author
------
dbonadiman

"""
import sys


def words(s):
    """
    words
    This function simpli split the string in spaces
    and counts the number of splits, it's a very
    simple and sometimes wrong.

    Parameters:
    s ==> the string from wich to count the vowels

    Test:

    >>> words('ciao come va')
    3

    >>> words('cat')
    1
    """
    return len(s.split(" "))


def main():
    try:
        print("\nThis program counts the words in a string\n"
              "Please enter the string: \n")
        string = raw_input("--> ")
        print(words(string))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
