"""
Problem
-------
**Complex Number Algebra**
Show addition, multiplication, negation,
and inversion of complex numbers in separate
functions. (Subtraction and division operations
can be made with pairs of these operations.)
Print the results for each operation tested.


Solution
--------
The solution is organized in two different
functions:
the first takes the real number and
produces a tuple containing the real and the
immaginary part respectively.
The second ececute the operation + - * /
and returns the real number in the
"tuple - form"


Author
------
dbonadiman

"""
# TODO: Integrate this with the calculator problem
# TODO: Use a grammar to pares expression and execute
#       operation recursively
import sys


def evaluate(a, b, o):
    """
    evaluate

    This function evaluate some operation
    between complex numbers

    Parameters:

    a ==> a tuple in which the first element
          is the real part and the second element
          is the immaginary part
    b ==> a tuple in which the first element
          is the real part and the second element
          is the immaginary part
    o ==> the operand that must be an string in
          set "+-*/"

    Test:

    >>> evaluate((1.0, 3.0), (3.0, 1.0), '+')
    (4.0, 4.0)

    >>> evaluate((1.0, 3.0), (3.0, 1.0), '-')
    (-2.0, 2.0)

    >>> evaluate((1.0, 3.0), (3.0, 1.0), '*')
    (0.0, 10.0)

    >>> evaluate((1.0, 3.0), (3.0, 1.0), '/')
    (0.0, 1.0)

    >>> evaluate((1.0, 3.0), (3.0, 1.0), '^')
    Traceback (most recent call last):
    ...
    ValueError: Only +, -, * and / allowed
    """
    if o not in "+-*/":
        raise ValueError("Only +, -, * and / allowed")
    if o == "+":
        return (a[0]+b[0], a[1]+b[1])
    if o == "-":
        return (a[0]-b[0], a[1]-b[1])
    if o == "*":
        return ((a[0]*b[0]-a[1]*b[1]), (a[0]*b[1]+a[1]*b[0]))
    if o == "/":
        return ((a[0]*b[0]-a[1]*b[1])/(b[0]*b[0]+b[1]*b[1]),
                (a[0]*b[1]+a[1]*b[0])/(b[0]*b[0]+b[1]*b[1]))


def complex_to_tuple(inp):
    """
    complex_to_tuple

    This function took in input a complex number
    in string format and outputs the corresponding
    tuple (real, immaginary)

    Parameters:

    inp ==> The number in string format expected

    Test:

    >>> complex_to_tuple('3 + 2i')
    (3.0, 2.0)

    >>> complex_to_tuple('2i + 3')
    (3.0, 2.0)

    >>> complex_to_tuple('2i +')
    Traceback (most recent call last):
    ...
    ValueError: Only n + mi and ni + m numbers accepted

    >>> complex_to_tuple('')
    Traceback (most recent call last):
    ...
    ValueError: Only n + mi and ni + m numbers accepted
    """
    try:
        tup = str(inp).split("+")
        if 'i' in tup[0]:
            return (float(tup[1]), float(tup[0].replace('i', '')))
        else:
            return (float(tup[0]), float(tup[1].replace('i', '')))
    except:
        raise ValueError("Only n + mi and ni + m numbers accepted")


def main():
    try:
        print("\nThis program execute operation between complex numbers\n"
              "Please insert the two number to operate with "
              "(in the form n + mi) and then the operator (+, -, *, /).\n")

        a = complex_to_tuple(str(raw_input("-- > ")))
        b = complex_to_tuple(str(raw_input("-- > ")))
        o = raw_input("--> ")

        r = evaluate(a, b, o)
        print("{} + {}i".format(r[0], r[1]))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
