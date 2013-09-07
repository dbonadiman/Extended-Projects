"""
Problem
-------
**Distance Between Two Cities**
Calculates the distance between two cities
and allows the user to specify a unit of
distance. This program may require finding
coordinates for the cities like latitude
and longitude.


Solution
--------
solution found using the geopy library


Author
------
dbonadiman

"""

import sys
from math import fabs, acos, pi, sin, cos, radians
from geopy import geocoders


def geo_distance(a, b):
    """
    This calculate the distance between two geographical
    coordinates

    >>> geo_distance((46.06, 11.12), (46.49, 11.35))
    47.81381845713197

    """

    R = 6371  # Earth radius
    a_rad = (radians(a[0]), radians(a[1]))
    b_rad = (radians(b[0]), radians(a[1]))
    fi = fabs(a_rad[1] - b_rad[1])
    p = acos(sin(b_rad[0]) * sin(a_rad[0])
             + cos(b_rad[0]) * cos(a_rad[0]) * cos(fi))
    return p*R


def main():
    try:
        print("\nThis program calculate the distance between two city\n"
              "Please enter the name of the cities:\n")
        gn = geocoders.GoogleV3()
        city1 = gn.geocode(raw_input("--> "), exactly_one=False)[0]
        city2 = gn.geocode(raw_input("--> "), exactly_one=False)[0]
        print("\nthe distance between {} and {} "
              "is : {} m").format(city1[0], city2[0],
                                  geo_distance(city1[1], city2[1]))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
