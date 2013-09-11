"""
Problem
-------
**Check if Palindrome**
Checks if the string entered by the user
is a palindrome. That is that it reads
the same forwards as backwards like racecar


Solution
--------
The solution is provided simply checking if the string
is equal to the same string reversed.



Author
------
dbonadiman

"""
import sys


def palindrome(s):
    """
    palindrome
    This function simply checks if the string
    is equals to itself reversed

    Parameters:
    s ==> the string

    Test:
    >>> palindrome('racecar')
    True

    >>> palindrome('ciao')
    False
    """
    return s == s[::-1]


def main():
    try:
        print("\nThis program checks if a sting is palindrome\n"
              "Please enter the string you want to check: \n")
        string = raw_input("--> ")
        print('')
        print(palindrome(string))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
