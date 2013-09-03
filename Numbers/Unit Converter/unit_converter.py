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
        global input
        try: input = raw_input
        except NameError: pass
        f = input("From (C,K,F): ")
        t = input("To (C,K,F): ")
        a = float(input("Amount: "))
    except Exception:
        print("Wrong input,retry.")
        main()
    else:
        print (_temp[f+"_"+t](a))

if __name__=="__main__":
    main()
