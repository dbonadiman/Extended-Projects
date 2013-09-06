"""
Problem
-------

**Unit Converter (temp, currency, volume, mass and more)**
Converts various units between one another. The user enters
the type of unit being entered, the type of unit they want
to convert to and then the value. The program will then
make the conversion.

Solution
--------
I'm gonna use a dictionary of lambda function to solve this
problem.
It's works only for temperature.
It's possible to add more conversions adding the functions into
the dictionary

Author
------
dbonadiman

"""
import sys

"""
>>> _temp['C_K'](10)
283.15


>>> _temp['F_C'](80)
26.666666666666668
"""

_temp = {
    'C_K': lambda c: c+273.15,
    'K_C': lambda k: k-273.15,
    'C_F': lambda c: c*9.0/5.0+32.0,
    'F_C': lambda f: (f-32.0)*5.0/9.0,
    'F_K': lambda f: ((f-32.0)*5.0/9.0)+273.15,
    'K_F': lambda k: ((k-273.15)*9.0/5.0)+32.0
}


def main():
    try:
        f = raw_input("From (C,K,F): ")
        t = raw_input("To (C,K,F): ")
        a = float(input("Amount: "))
    except Exception:
        print("You have entered a non valid input")
        return 1
    else:
        print (_temp[f+"_"+t](a))
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
