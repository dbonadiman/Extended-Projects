"""
Problem
-------
**Vigenere / Vernam / Ceasar Ciphers**
Functions for encrypting and decrypting data
messages. Then send them to a friend.



Solution
--------
Implementation of the 3 chipers

Author
------
dbonadiman

"""
import sys
import random


def cesar_enc(s, i=4):
    """
    cesar encript
    An implementation of the cesar chiper

    Parameter:
    s ==> the string to encript must be in lower case

    i ==> the cesar encoder parameter that represent
          the number of position in the dictionary to
          add to each character in the string

    Test:
    >>> cesar_enc('ciao')
    'gmes'

    >>> cesar_enc('a',1)
    'b'
    """
    return ''.join([chr(((ord(c)-ord('a')+i) % 26)+ord('a'))
                    if ord(c) >= ord('a') and ord(c) <= ord('z')
                    else c for c in s])


def cesar_dec(s, i=4):
    """
    cesar decript
    this function decripts the encoded message,
    it basically apply tje cesar enc function
    using - the key

    Parameter:
    s ==> the string to encript must be in lower case

    i ==> the cesar decoder parameter that represent
          the number of position in the dictionary to
          add to each character in the string

    Test:
    >>> cesar_dec('gmes')
    'ciao'

    >>> cesar_dec('b',1)
    'a'
    """
    return cesar_enc(s, -i)


def vigenere_enc(s, key):
    """
    vigenere enc

    this function encripts a stirng using the
    vigenere cipher this works like the cesar cipher with the
    difference that it uses a string key to encript
    the message

    Parameter:
    s ==> the string to encript

    key ==> a string to use as password

    Test:
    >>> vigenere_enc('ciao','lemon')
    'nmmc'

    >>> vigenere_enc('aaaaa','lemon')
    'lemon'
    """
    return ''.join(cesar_enc(s[i],
                   ord(key[i % len(key)]) % ord('a'))
                   for i in range(len(s)))


def vigenere_dec(s, key):
    """
    vigenere enc

    this function decripts a stirng using the
    vigenere cipher this works like the cesar cipher with the
    difference that it uses a string key to encript
    the message

    Parameter:
    s ==> the string to encript

    key ==> a string to use as password

    Test:
    >>> vigenere_dec('nmmc','lemon')
    'ciao'

    >>> vigenere_dec('lemon','lemon')
    'aaaaa'
    """
    return ''.join(cesar_dec(s[i],
                   ord(key[i % len(key)]) % ord('a'))
                   for i in range(len(s)))


def get_random_key(s):
    """
    get random key
    this will generate a random key to use in the vernam cipher

    Is it not possible to test it
    """
    return [chr(random.randint(ord('a'), ord('z')))
            if (ord(c) >= ord('a') and ord(c) <= ord('z'))
            else c for c in s]


def vernam_enc(s, key):
    """
    vernam enc

    This works like the vigenere enc
    with the difference that it uses a pass key generate at random
    of the same lenght of the string to encript
    """
    assert len(s) == len(key)

    return vigenere_enc(s, key)


def vernam_dec(s, key):
    """
    vernam enc

    This works like the vigenere dec
    with the difference that it uses need a pass key
    of the same lenght of the string to encript
    """
    assert len(s) == len(key)

    return vigenere_dec(s, key)


def main():
    try:
        print("\nThis program encript a word you enter "
              "using mant different cipher\n"
              "Please enter the string: \n")
        text = raw_input("-->")
        text = text.lower()
        print("\nCesar: {}".format(cesar_enc(text, 4)))
        print(cesar_dec(cesar_enc(text, 4), 4) == text)
        print("\nVigenere: {}".format(vigenere_enc(text, "lemon")))
        print(vigenere_dec(vigenere_enc(text, "lemon"), "lemon") == text)
        key = get_random_key(text)
        print("\nVernam: {}".format(vernam_enc(text, key)))
        print(vernam_dec(vernam_enc(text, key), key) == text)
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
