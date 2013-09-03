def reverse(s):
    return s[::-1]

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        string = input("")
    except Exception:
        print("Wrong input, retry.")
        main()
    else:
        print(reverse(string))

if __name__=="__main__":
    main()