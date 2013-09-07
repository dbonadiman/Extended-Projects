"""
Problem
-------
**Alarm Clock**
A simple clock where it plays
a sound after X number of minutes/seconds
or at a particular time.


Solution
--------

This solution is provided using the "bip"
of the console


Author
------
dbonadiman

"""

import sys
import time


#TODO: find a better way to play the sound
def alarm(n):
    for i in range(n):
        print('\a')
        time.sleep(0.2)
    print()


def main():
    try:
        seconds = int(raw_input("seconds:"))
        time.sleep(seconds)
        alarm(20)
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
