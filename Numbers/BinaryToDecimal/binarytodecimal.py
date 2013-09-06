"""
Problem
-------
**Binary to Decimal and Back Converter**

Develop a converter to convert a decimal
number to binary or a binary number to
its decimal equivalent.


Solution
--------
The converter is implemented using strings
to represent the bynary numbers

Author
------
dbonadiman

"""
import sys


def decimal_to_binary(num):
    """
    Converts a decimal number to a binary
    sting

    >>> decimal_to_binary(3)
    '11'

    >>> decimal_to_binary(0)
    ''

    >>> decimal_to_binary(15)
    '1111'
    """
    binary = []
    while num > 0:
        binary.append(str(num % 2))
        num = int(num/2)
    return "".join(binary[::-1])


def binary_to_decimal(bin):
    """
    Converts a binary string to a real number!

    >>> binary_to_decimal('11')
    3

    >>> binary_to_decimal('')
    Traceback (most recent call last):
        ...
    ValueError: No number to process!!!

    >>> binary_to_decimal('3')
    Traceback (most recent call last):
        ...
    ValueError: A binary string was expected

    """
    dec = []
    if not bin:
        raise ValueError('No number to process!!!')
    for i, v in enumerate(bin[::-1]):
        if v not in '10':
            raise ValueError('A binary string was expected')
        if int(v):  # 1 is True and 0 is False
            dec.append((2)**(i))
    return sum(dec)


def main():
    try:
        print("\nThis program converts decimal number to binary"
              "and vice-versa.")

        decimal = int(raw_input("\nA decimal number: "))
        print (decimal_to_binary(decimal))
        binary = str(raw_input("\nA binary string: "))
        print (binary_to_decimal(binary))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
