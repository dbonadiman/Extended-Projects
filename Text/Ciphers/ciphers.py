import random

_dic = {}

def cesar_enc(s,i):
    return ''.join([chr(((ord(c)-ord('a')+i)%26)+ord('a')) if ord(c)>=ord('a') and ord(c)<=ord('z') else c for c in s])

def cesar_dec(s,i):
    return ''.join([chr(((ord(c)-ord('a')-i)%26)+ord('a')) if (ord(c)>=ord('a') and ord(c)<=ord('z')) else c for c in s])

def vigenere_enc(s,key, out = None):
    if out is None:
        out = ""
    return ''.join(cesar_enc(s[i],ord(key[i%len(key)])%ord('a')) for i in range(0,len(s)))

def vigenere_dec(s,key, out = None):
    if out is None:
        out = ""
    return ''.join(cesar_dec(s[i],ord(key[i%len(key)])%ord('a')) for i in range(0,len(s)))

def get_key(s):
    return _dic.get(s,[chr(random.randint(ord('a'),ord('z'))) if (ord(c)>=ord('a') and ord(c)<=ord('z')) else c for c in s])

def vernam_enc(s,key):
    return vigenere_enc(s,key)

def vernam_dec(s,key):
    return vigenere_dec(s,key)

def main():
    try:
        global input
        try: input = raw_input
        except NameError: pass
        text = str(input(""))
    except Exception:
        print("Wrong input,retry.")
        main()
    else:
        text =  text.lower()
        print(cesar_enc(text,4))
        print(cesar_dec(cesar_enc(text,4),4)==text)
        print(vigenere_enc(text,"lemon"))
        print(vigenere_dec(vigenere_enc(text,"lemon"),"lemon")==text)
        key = get_key(text)
        print(vernam_enc(text,key))
        print(vernam_dec(vernam_enc(text,key),key)==text)

if __name__=="__main__":
    main()