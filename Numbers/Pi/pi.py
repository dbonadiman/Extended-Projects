
###########################
# More precision is needed.
# 
#
#
#
###########################
import sys

def pi():
    return 2*opi(1,60)

def opi(i,loops):
    if i==loops:
        return 1
    else:
        n = 1.0 + i / (2.0 * i + 1) * opi(i + 1,loops)
        return n

def main():
    global input
    try: input = raw_input
    except NameError: pass
    outstring = 'The Number is {:.'+str(int(input("Precision:"))+1)+'}'
    print(outstring.format(pi()))

if __name__=="__main__":
    main()
