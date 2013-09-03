def words(s):
    return len([word for word in s.split(" ") if word not in ".,?!"] )

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        text = input("")
    except Exception:
        print("Wrong input,retry.")
        main()
    else:
        print(words(text))

if __name__=="__main__":
    main()