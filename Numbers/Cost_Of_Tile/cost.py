"""
Problem
-------
**Find Cost of Tile to Cover W x H Floor**

Calculate the total cost of tile it would take to
cover a floor plan of width and height, using a
cost entered by the user.


Solution
--------
A simple function that multiplies cost, width and height

Author
------
dbonadiman

"""
import sys


def cost_of_tile(cost, width, height):
    """
    This function compute the cost of tile
    given a cost, a width and an height
    
    >>> cost_of_tile(10.0, 10.1, 2)
    202.0

    >>> cost_of_tile(2.0, 0, 10)
    0.0
    """
    return cost*width*height

        
def main():
    price = float(raw_input("What's the cost for sqared meter ($)? "))
    width = float(raw_input("What's the width of the floor? "))
    height = float(raw_input("What's the height of the floor? "))
    print ("The cost of tile is {} $ ".format(cost_of_tile(price, width, height)))
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
    


