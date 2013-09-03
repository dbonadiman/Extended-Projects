def reverse(s):
    return s[::-1]

def main():
    try:
        string = input("")
    except Exception:
        print("Wrong input, retry.")
        main()
    else:
        print(reverse(string))


if __name__=="__main__":
    main()