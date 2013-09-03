def palindrome(s):
    for i in range(0,len(s)):
        if s[i]!=s[(len(s)-1)-i]:
            return False
    return True

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        string = str(input(""))
    except Exception:
        print("Wrong input, retry.")
        main()
    else:
        print(palindrome(string))

if __name__=="__main__":
    main()