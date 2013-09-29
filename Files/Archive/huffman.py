"""
Problem
-------
** Huffman Encoding **


Solution
--------
Here is presented a version of the huffman encoding algorithm

Author
------
dbonadiman

"""


def encode(st):
    """
    The encode function it takes in input a string and outputs a pair
    consisting of the encripted string and the dictionary used to convert
    it

    Parameters
    ---------

    st => the string to encode.

    """
    def _remove_count(c):
        """
        This method removes from the built huffman tree the occurrences
        count.

        ----
        Parameters

        c => the huffman tree
        """
        if not type(c[0]) is tuple:
            return (c[0])
        else:
            return (_remove_count(c[0][0]), _remove_count(c[0][1]))

    def _traverse(ht,s):
        """
        A recursive method used to convert the huffman tree into
        a dictionary.

        Parameters
        -----------
        ht => the huffman tree pruned from the occurrences counts
        s => the current string of 0 and 1
        """
        if type(ht) is str:
            return {ht:s}
        else:
            d1 = _traverse(ht[0],s+'0')
            d1.update(_traverse(ht[1],s+'1'))
            return d1

    char_set = set(st)
    tuples = [(c,st.count(c)) for c in char_set]

    #Creation of the huffman tree
    while True:
        tuples =sorted(tuples, key= lambda a:a[1], reverse=True)
        m = tuples.pop()
        n = tuples.pop()
        tuples.append(((m,n),m[1]+n[1]))
        if len(tuples) == 1:
            break

    # Convertion of the huffman tree to a dictionary
    d = _traverse(_remove_count(tuples[0]),'')

    #Substitute each character with the corresponding bit string
    bit_list = ''.join([d[c] for c in st])

    #Convertion of the bit string to a bytearray
    b = bytearray([int(bit_list[x:x+8], 2) for x in range(0, len(bit_list), 8)])
    return (b,d)


def decode((st,r_d)):
    """
    The decode function first revert the dictionary and then for each group
    of bit subsitute the corresponding character from the dictionary

    Parameters
    -------------
    (st,r_d) => A pair composet from an encripted string st and a r_d that
                is the dictionary used to encript the string.
    """
    from collections import OrderedDict
    d_t = dict(zip(r_d.values(),r_d.keys()))
    d = OrderedDict(sorted(d_t.items(), key=lambda t: len(t[0])))
    string = []
    buff = ''
    for s in st:
        bin_st = bin(ord(s))[2:].zfill(8)
        for b in bin_st:
            if buff in d:
                string.append(d[buff])
                buff = b
            else:
                buff += b
    return ''.join(string)



def main():
    import cPickle
    st = open('files/pride_and_prejudice.txt','r').read()
    r = encode(st)
    open('pride.huff','wb').write(r[0])
    cPickle.dump(r[1],open('pride.ht','wb'))
    st = open('pride.huff','r').read()
    ht = cPickle.load(open('pride.ht','rb'))
    print decode((st,ht))

    return 0



if __name__ == "__main__":
    main()
