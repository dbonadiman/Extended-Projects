import sys
from math import fabs,acos,pi,sin,cos,radians
from geopy import geocoders

def _setup():
    global input
    try: input = raw_input
    except NameError: pass

def euclidean_distance(a,b):
    R = 6371
    a_rad = (radians(a[0]),radians(a[1]))
    b_rad = (radians(b[0]),radians(a[1]))
    fi = fabs(a_rad[1] - b_rad[1])
    p = acos(sin(b_rad[0]) * sin(a_rad[0]) + cos(b_rad[0]) * cos(a_rad[0]) * cos(fi))
    return p*R
    
def main():
    gn = geocoders.GoogleV3()
    city1  = gn.geocode(input("-->"), exactly_one=False)[0]
    city2  = gn.geocode(input("-->"), exactly_one=False)[0]  
    print("the distance between {} and {} is : {} ").format(city1[0],city2[0],euclidean_distance(city1[1],city2[1]))

if __name__=="__main__":
    _setup()
    status = main()
    sys.exit(status)
    
