"""
Problem
-------
**Number Names**
Show how to spell out a number in English.
You can use a preexisting implementation
or roll your own, but you should support
inputs up to at least one million (or the maximum
value of your language's default bounded integer
type, if that's less). *Optional: Support for
inputs other than positive integers
(like zero, negative integers, and
floating-point numbers).*


Solution
--------
The solution is provided in a recursive way.
Using a dictionary mapping the number with the
related name

Author
------
dbonadiman

"""
import sys


def digit_to_name(n):
    """
    digit_to_name

    This recursive function takes in input a number
    and outputs the name of the number in english

    Parameters:
    n ==> The number in input(it must be and integer)

    Test:

    >>> digit_to_name(3)
    'three'

    >>> digit_to_name(33)
    'thirty-three'
    """
    onetotwenty = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fiveteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    dec = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    uptotrillion = {
        1000000000000: "trillion",
        1000000000: "billion",
        1000000: "million",
        1000: "thousand",
        100: "hundred"
    }

    for dig in uptotrillion:
        if int(n/dig) != 0:
            if n % dig == 0:
                return "".join([digit_to_name(int(n / dig)),
                                " ", uptotrillion[dig]])
            else:
                return "".join([digit_to_name(int(n / dig)),
                                " ", uptotrillion[dig],
                                " ", digit_to_name(n % dig)])

    if n < 100 and n >= 20:
        for dig in dec:
            if n-dig < 10 and n-dig > 0:
                return "".join([dec[dig], "-", digit_to_name(n-dig)])
            elif not n-dig:
                return dec[dig]

    return onetotwenty[n]


def main():
    try:
        print("\nThis program takes in input an integer and outputs\n"
              "the number's name in english\n"
              "Please enter the number:\n")
        n = int(raw_input("-->"))
        if not n:
            raise ValueError("Only numbers greather than 0 allowed")
        print(digit_to_name(n))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
