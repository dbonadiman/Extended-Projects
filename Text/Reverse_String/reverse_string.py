"""
Problem
-------
**Reverse a String**
Enter a string and the program
will reverse it and print it out.


Solution
--------
This problem is quite simple and
can be solved using the string as a list
and reverse it.
For visual way i kept a separate functions
but it's not necessary cause what you need
to reverse a string is about 6 character long

Author
------
dbonadiman

"""
import sys


def reverse(s):
    """
    reverse
    This function reverse a string it uses the same
    approach used to manipulate lists

    Parameters:

    s==> the string to reverse

    Test:

    >>> reverse('ciao')
    'oaic'

    >>> reverse('oil')
    'lio'

    >>> reverse('')
    ''

    """
    return s[::-1]


def main():
    try:
        print("\nThis program reverse a string\n"
              "please enter the string you want to reverse: \n")
        string = raw_input("-->")
        print(reverse(string))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
