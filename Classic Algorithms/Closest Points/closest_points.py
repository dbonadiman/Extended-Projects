import sys
import math

def distance(a,b):
    if len(a)!=len(b):
        raise ValueError()
    else:
        return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))    

def closest_pair(points):
    minim =((),float("inf"))
    for a in points:
        for b in points:
            if a is not b and distance(a,b)<minim[1]:
                minim = ((a,b),distance(a,b))
    return minim[0]
                
def main():
    points = [(1,2),(3,2),(1,10),(2,1)]
    print closest_pair(points)

if __name__=="__main__":
    status = main()
    sys.exit(status)