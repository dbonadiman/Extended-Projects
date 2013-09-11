"""
Problem
-------
**Count Vowels**
Enter a string and the program counts
the number of vowels in the text.
For added complexity have it report a
sum of each vowel found.


Solution
--------
The solution is provided using a lambda function

Author
------
dbonadiman

"""
import sys


def vowels(s):
    """
    vowels
    This solution uses a lambda function that
    sums one if the first letter of the word is a vowel,
    zero othrerwise and then recursively on the rest of the word.

    There is a funny optimisation using the fact that in
    python boolean and integer are actually the same thing
    so we actually sum the condition instead of extensively
    write

    if condition:
        return A+1
    else:
        return A

    we use this compact form

    return A+condition

    Parameters:
    s ==> the string from wich to count the vowels

    Test:

    >>> vowels('ciao')
    3

    >>> vowels('cat')
    1

    >>> vowels('mmm')
    0
    """

    #Python is fuking awesome
    i = lambda s: i(s[1:])+(s[0] in "aeiou") if len(s) else 0
    return i(s)


def main():
    try:
        print("\nThis program counts the vowels in a string\n"
              "Please enter the string: \n")
        string = raw_input("--> ")
        print(vowels(string))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
