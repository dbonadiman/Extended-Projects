import struct

HUFFMAN = 0
LZW16 = 1
LZW32 = 2
MTF = 3


class Huffman(object):

	__input =""
	__ht = (((((((14, (220, 230)), ((156, 223), 17)), (((191, 201), (235, 250)), ((196, 181), (202, 188)))), ((((164, 208), (229, 175)), ((210, 179), (151, 159))), (((226, 205), (187, 145)), ((251, 186), (153, 124))))), (((((139, 157), (239, 161)), ((246, 137), (168, 207))), ((16, (255, 194)), (12, 19))), ((((213, 155), (141, 158)), ((142, 152), 20)), (((131, 222), (146, 123)), ((195, 218), (171, 206)))))), ((((((169, 160), (163, 134)), ((231, 185), (247, 192))), (((173, 136), (177, 130)), ((190, 118), (128, 167)))), ((((193, 140), (96, 182)), ((172, 148), (126, 203))), (((180, 133), (214, 147)), ((211, 113), (178, 102))))), (((((129, 97), (106, 135)), ((79, 122), (117, 144))), ((10, (165, 127)), ((215, 109), (114, 138)))), (((8, (87, 199)), ((149, 93), (104, 81))), (((92, 94), (132, 86)), ((120, 125), (105, 111))))))), (((((1, ((162, 110), (100, 103))), (((91, 82), 9), ((116, 143), (150, 112)))), ((((64, 108), (174, 68)), (6, (83, 90))), (((107, 121), (88, 119)), ((85, 115), (73, 75))))), (((((95, 72), 7), ((63, 101), 2)), (((80, 77), (74, 66)), ((99, 84), 5))), ((((61, 51), (76, 69)), ((59, 58), (67, 98))), (((70, 71), (89, 78)), ((60, 62), (54, 53)))))), ((((((57, 48), (50, 35)), ((36, 40), 0)), (((55, 37), (47, 52)), ((43, 46), (65, 41)))), ((((45, 34), (38, 49)), ((33, 31), (42, 30))), (((25, 28), (56, 21)), (4, (44, (240, 234)))))), (((((39, 26), (29, (225, 237))), ((22, 24), 3)), (((27, (184, 232)), (32, (233, 242))), ((11, (224, 241)), ((254, 236), (253, 228))))), (((((204, 189), 18), ((197, 249), (219, 245))), (((176, 212), (227, 238)), ((209, 216), 13))), (((15, (154, 217)), ((183, 243), (170, 248))), (((221, 200), (252, 198)), (23, (166, 244)))))))))

	def __init__(self,data):
		self.__input=data
		
	def __chunks(self,l, n):
		return [l[i:i+n] for i in range(0, len(l), n)]
		
	def __bit_to_char(self,bit_str):
		out = []
		for b in self.__chunks(bit_str,8):
			if len(b) < 8:
				b = b + '0' * (8 - len(b))
			out+=[int(b, 2)]
		return out

	def __char_to_bit(self,string):
		out = ''
		for c in string:
			if  isinstance(c, str):
				c = ord(c)
			out += '{0:08b}'.format(c)
		return out

	def __dump_data(self,data):
		import pickle
		out = pickle.dumps(data)
		return out


	def __loads_data(self,st):
		import pickle
		data = pickle.loads(st)
		return data



	def __ht_from_st(self,st):
		from  operator import itemgetter

		chars = set(st)
		tuples = [(c,st.count(bytearray([c]))) for c in chars]
		while len(tuples)>1:
			m = min(tuples, key=itemgetter(1))
			tuples.remove(m)
			n = min(tuples, key=itemgetter(1))
			tuples.remove(n)
			tuples += [((m,n),m[1]+n[1])]
		return self.__remove_count(tuples[0])

	def __remove_count(self,c):
		if not isinstance(c,tuple):
			raise Exception("{} is not a tuple".format(c))
		if isinstance(c[0],tuple):
			return (self.__remove_count(c[0][0]),self.__remove_count(c[0][1]))
		else:
			return (c[0])

	def __traverse(self,ht,s=""):
		if not isinstance(ht,tuple):
			return {ht:s}
		else:
			d1 = self.__traverse(ht[0],s+'0')
			d1.update(self.__traverse(ht[1],s+'1'))
			return d1

	def encode(self):
		ht = self.__ht
		
		conversion_table = self.__traverse(ht)
		s = "".join([conversion_table[c] for c in self.__input])
		b =self.__bit_to_char(s)
		return bytearray(b)


	def decode(self):
		#data = self.__loads_data(self.__input)
		string =bytearray()
		t = self.__ht
		for s in self.__char_to_bit(self.__input):
			if isinstance(t[int(s)], tuple):
				t = t[int(s)]
			else:
				string += bytearray([t[int(s)]])
				t = self.__ht
		return string


class LZW(object):

	__input =""
	__bit = 16
	
	__b = {
		16: "!H",
		32: "!I",
		64: "!Q"
	}

	def __init__(self,data,bit=16):
		self.__input=data
		self.__bit=bit


	def encode(self):
		dict_size = 256
		#dictionary = dict((chr(i), chr(i)) for i in xrange(dict_size))
		dic = {str([i]): i for i in range(dict_size)}
		out_st = bytearray()
		buff = []
		for s in bytearray(self.__input):
			buffers = buff+[s]
			if str(buffers) in dic:
				buff = buffers
			else:
				out_st+=struct.pack(self.__b[self.__bit], dic[str(buff)])
				if dict_size<2**self.__bit:
					dic[str(buffers)] = dict_size
					dict_size += 1
				buff = [s]
		if buff:
			out_st+=struct.pack(self.__b[self.__bit], dic[str(buff)])
		return out_st

	def __chunks(self,l, n):
		return [l[i:i+n] for i in range(0, len(l), n)]

	def decode(self):
		dict_size = 256
		#dictionary = dict((chr(i), chr(i)) for i in xrange(dict_size))
		dic = {i: [i] for i in range(dict_size)}
		array = [struct.unpack(self.__b[self.__bit], s)[0] for s in self.__chunks(self.__input, self.__bit/8)]
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
		
		
class MTFT(object):

	def __init__(self,data):
		self.__input=data


	def encode(self):
		dict_size = 256
		l = [i for i in range(dict_size)]
		out_st = []
		for s in bytearray(self.__input):
			old_index = l.index(s)
			l.insert(0, l.pop(old_index))
			out_st+=[old_index]		
		return bytearray(out_st)

	def decode(self):
		dict_size = 256
		l = [i for i in range(dict_size)]
		out_st = []
		for s in bytearray(self.__input):
			st = l.pop(s)
			l.insert(0, st)
			out_st+=[st]		
		return bytearray(out_st)



		

def instance(c,st):
	if c==0:
		return Huffman(st)
	if c==1:
		return LZW(st,16)
	if c==2:
		return LZW(st,32)
	if c==3:
		return MTFT(st)
	print(c)


def __test():
	import pickle
	s = open('files/pride_and_prejudice.txt','rb').read()
	print(len(s))
	#print 100
	enc = s

	enc = LZW(enc,16).encode()
	print(len(enc))
	enc = Huffman(enc).encode()
	print(len(enc))
	enc =Huffman(enc).decode()
	print(len(enc))
	enc =LZW(enc,16).decode()
	print(len(enc))

	if not s==enc:
		print('Decoding Error')
		open('error.log.txt','wb').write(enc)

	




def __main():
	__test()


if __name__=="__main__":
	__main()