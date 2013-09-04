import sys

def luhn_formula(number):
    return sum(int(n) if i%2==0 else sum(int(d) for d in str(int(n)*2)) for (i,n) in enumerate(number[::-1].replace(' ','')))%10 == 0
        
def main():
    print(luhn_formula("479410028 3427946"))
    print(luhn_formula("4556295908122936"))
    print(luhn_formula("6011333579009589"))
    print(luhn_formula("379408169807839"))
    print(luhn_formula("4916768258178471"))
    print(luhn_formula("6011273169891659"))
    return 0  

if __name__=="__main__":
    status = main()
    sys.exit(status)