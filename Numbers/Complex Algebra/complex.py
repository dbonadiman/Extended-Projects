import sys

def eval(a,b,o):
    print a
    print b
    if o == "+":
        return (a[0]+b[0], a[1]+b[1])
    if o == "-":
        return (a[0]-b[0], a[1]-b[1])
    if o == "*":
        return ((a[0]*b[0]-a[1]*b[1]), (a[0]*b[1]+a[1]*b[0]))
    if o == "/":
        return ((a[0]*b[0]-a[1]*b[1])/(b[0]*b[0]+b[1]*b[1]), (a[0]*b[1]+a[1]*b[0])(b[0]*b[0]+b[1]*b[1]))

def complex_to_tuple(inp):
    try:
        tup = str(inp).split("+")
        if 'i' in tup[0]:
            return (float(tup[1]),float(tup[0].replace('i',''))) 
        else:
            return (float(tup[0]),float(tup[1].replace('i','')))
    except:
        raise ValueError("Only n + mi and ni + m numbers accepted")
        
def main():
    a = complex_to_tuple(str(input("a -- > ")))
    b = complex_to_tuple(str(input("b -- > ")))
    o = input("o --> ")
    r = eval(a,b,o)
    print("{} + {}i".format(r[0],r[1]))

if __name__=="__main__":
    global input
    try: input = raw_input
    except NameError: pass
    status = main()
    sys.exit(status)