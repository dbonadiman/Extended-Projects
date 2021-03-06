class _Huffman(object):
    _input = ""
    _ht = (((((((14, (220, 230)), ((156, 223), 17))
            , (((191, 201), (235, 250)), ((196, 181), (202, 188))))
            , ((((164, 208), (229, 175)), ((210, 179), (151, 159)))
            , (((226, 205), (187, 145)), ((251, 186), (153, 124)))))
            , (((((139, 157), (239, 161)), ((246, 137), (168, 207)))
            , ((16, (255, 194)), (12, 19))), ((((213, 155), (141, 158))
            , ((142, 152), 20)), (((131, 222), (146, 123)), ((195, 218)
            , (171, 206)))))), ((((((169, 160), (163, 134)), ((231, 185)
            , (247, 192))), (((173, 136), (177, 130)), ((190, 118), (128, 167))))
            , ((((193, 140), (96, 182)), ((172, 148), (126, 203))), (((180, 133)
            , (214, 147)), ((211, 113), (178, 102))))), (((((129, 97), (106, 135))
            , ((79, 122), (117, 144))), ((10, (165, 127)), ((215, 109), (114, 138))))
            , (((8, (87, 199)), ((149, 93), (104, 81))), (((92, 94), (132, 86)), ((120, 125)
            , (105, 111))))))), (((((1, ((162, 110), (100, 103))), (((91, 82), 9), ((116, 143)
            , (150, 112)))), ((((64, 108), (174, 68)), (6, (83, 90))), (((107, 121), (88, 119))
            , ((85, 115), (73, 75))))), (((((95, 72), 7), ((63, 101), 2)), (((80, 77), (74, 66))
            , ((99, 84), 5))), ((((61, 51), (76, 69)), ((59, 58), (67, 98))), (((70, 71), (89, 78))
            , ((60, 62), (54, 53)))))), ((((((57, 48), (50, 35)), ((36, 40), 0)), (((55, 37), (47, 52))
            , ((43, 46), (65, 41)))), ((((45, 34), (38, 49)), ((33, 31), (42, 30))), (((25, 28), (56, 21))
            , (4, (44, (240, 234)))))), (((((39, 26), (29, (225, 237))), ((22, 24), 3)), (((27, (184, 232))
            , (32, (233, 242))), ((11, (224, 241)), ((254, 236), (253, 228))))), (((((204, 189), 18), ((197, 249)
            , (219, 245))), (((176, 212), (227, 238)), ((209, 216), 13))), (((15, (154, 217)), ((183, 243)
            , (170, 248))), (((221, 200), (252, 198)), (23, (166, 244)))))))))


    def __init__(self,data,bit = 8):
        try:
            self._input = bytearray(data)
        except Exception:
            self._input = data

    def _chunks(self,l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def _bit_to_char(self,bit_str):
        return [int(b,2) if len(b)==8 else int(b + '0' * (8 - len(b)),2) for b in self._chunks(bit_str,8)]

    def _char_to_bit(self,string):
        return ''.join('{0:08b}'.format(c) for c in string)

    def _traverse(self,ht,s=None):
        if s is None:
            s = ""
        if not isinstance(ht,tuple):
            return {ht:s}
        else:
            d1 = self._traverse(ht[0],s+'0')
            d1.update(self._traverse(ht[1],s+'1'))
            return d1

    def encode(self):
        ht = self._ht
        conversion_table = self._traverse(ht)
        s = "".join([conversion_table[c] for c in self._input])
        b =self._bit_to_char(s)
        return bytearray(b)

    def decode(self):
        string =bytearray()
        t = self._ht
        for s in self._char_to_bit(self._input):
            if isinstance(t[int(s)], tuple):
                t = t[int(s)]
            else:
                string += bytearray([t[int(s)]])
                t = self._ht
        return string


class _LZW(object):

    _input =""
    _bit = 16

    _b = {
        16: "!H",
        32: "!I",
        64: "!Q"
    }

    def __init__(self,data,bit=16):
        self._input=data
        self._bit=bit

    def encode(self):
        import struct
        dict_size = 256
        dic = {str([i]): i for i in range(dict_size)}
        out_st = bytearray()
        buff = []
        for s in bytearray(self._input):
            buffers = buff+[s]
            if str(buffers) in dic:
                buff = buffers
            else:
                out_st+=struct.pack(self._b[self._bit], dic[str(buff)])
                if dict_size<2**self._bit:
                    dic[str(buffers)] = dict_size
                    dict_size += 1
                buff = [s]
        if buff:
            out_st+=struct.pack(self._b[self._bit], dic[str(buff)])
        return out_st

    def _chunks(self,l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def decode(self):
        import struct
        dict_size = 256
        dic = {i: [i] for i in range(dict_size)}
        array = [struct.unpack(self._b[self._bit], s)[0] for s in self._chunks(self._input, int(self._bit/8))]
        out_st = pentry = dic[array.pop(0)]
        for ccode in array:
            if ccode in dic:
                entry =  dic[ccode]
            elif ccode==dict_size:
                entry = pentry+[pentry[0]]
            else:
                raise ValueError(str(ccode))
            out_st += entry
            dic[dict_size] = pentry+[entry[0]]
            dict_size +=1
            pentry = entry
        return bytearray(out_st)


class __MTFT(object):

    def __init__(self,data,bit=8):
        self._input=data

    def encode(self):
        dict_size = 256
        l = [i for i in range(dict_size)]
        out_st = []
        for s in bytearray(self._input):
            old_index = l.index(s)
            l.insert(0, l.pop(old_index))
            out_st+=[old_index]
        return bytearray(out_st)

    def decode(self):
        dict_size = 256
        l = [i for i in range(dict_size)]
        out_st = []
        for s in bytearray(self._input):
            st = l.pop(s)
            l.insert(0, st)
            out_st+=[st]
        return bytearray(out_st)

_instance = {
    0:lambda st:_Huffman(st),
    1:lambda st:_LZW(st,16),
    2:lambda st:_LZW(st,32),
    3:lambda st:_MTFT(st)
}

codecs = {
    "LZW16":[1],
    "LZW32":[2],
    "Huffman":[0],
    "DEFLATE":[1,0]
}


def encode(s,codec):
    codec = codecs[codec]
    for c in codec:
        s = _instance[c](s).encode()
    return s

def decode(s,codec):
    codec = codecs[codec][::-1]
    for c in codec:
        s = _instance[c](s).decode()
    return s

def _test():
    import pickle
    s = open('files/pride_and_prejudice.txt','rb').read()
    a = True
    for c in codecs.keys():
        print(c)
        enc = s
        enc = encode(s,c)
        dec = decode(enc,c)
        a = a and (dec == s)
    return a

def main():
    print(_test())
    return 0

if __name__=="__main__":
    import sys
    status = main()
    sys.exit(status)
