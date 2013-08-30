HUFFMAN = 0
LZW16 = 2
LZW24 = 3
LZW32 = 4


class Huffman(object):

	__input =""

	def __init__(self,data):
		self.__input=data
		
	def __chunks(self,l, n):
		return [l[i:i+n] for i in range(0, len(l), n)]
		
	def __bit_to_char(self,bit_str):
		out = ""
		for b in self.__chunks(bit_str,8):
			if len(b) < 8:
				b = b + '0' * (8 - len(b))
			out+=chr(int(b, 2))
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
		tmp = pickle.dumps(data[1])
		out=""
		out+=str(len(tmp))+"\n"
		out+=str(data[0])+"\n"
		if bytes is str:
			out+=tmp
			out+=data[2].decode("ISO-8859-1")
		else:
			out+=tmp.decode("ISO-8859-1")
			out+=data[2]
		return out


	def __loads_data(self,st):
		import pickle
		st = st.decode('utf-8')
		f = st.split('\n',2)
		data = f[0]
		size = int(data)
		d2 = f[1]
		leng = int(d2)
		data = f[2]
		return(leng,pickle.loads(data[:size].encode("ISO-8859-1")),data[size:].encode("ISO-8859-1"))



	def __ht_from_st(self,st):
		from  operator import itemgetter

		chars = set(st)
		tuples = [(c,st.count(c)) for c in chars]
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
		ht = self.__ht_from_st(self.__input)
		conversion_table = self.__traverse(ht)
		s = "".join([conversion_table[c] for c in self.__input])
		b =self.__bit_to_char(s)	
		return self.__dump_data((len(self.__input),ht,b))


	def decode(self):
		data = self.__loads_data(self.__input)
		string =""
		t = data[1]
		for s in self.__char_to_bit(data[2]):
			if isinstance(t[int(s)], tuple):
				t = t[int(s)]
			else:
				string += t[int(s)]
				t = data[1]
		return string[:data[0]]


class LZW(object):

	__input =""
	__bit = 16

	def __init__(self,data,bit=16):
		self.__input=data
		self.__bit=bit

	def __chunks(self,l, n):
		return [l[i:i+n] for i in range(0, len(l), n)]
		
	def __bit_to_char(self,bit_str):
		out = ""
		for b in self.__chunks(bit_str,8):
			if len(b) < 8:
				b = b + '0' * (8 - len(b))
			out+=chr(int(b, 2))
		return out

	def __char_to_bit(self,string):
		out = ''
		for c in string:
			out += '{0:08b}'.format(ord(c))
		return out


	def __decimal_to_chars(self, num, bit):
		binary = ""
		while num>0:
			binary+=str(num%2)
			num = int(num/2)
		if len(binary) < bit:
			binary += str(0)*(bit-len(binary))
		return self.__bit_to_char(binary[::-1])

	def __initialize_dic(self,bit):
		dic = {}
		for i in range(256):
			dic[chr(i)]=self.__decimal_to_chars(i,bit)
		return dic

	def __initialize_rev_dic(self,bit):
		dic = {}
		for i in range(256):
			dic[self.__decimal_to_chars(i,bit)]=chr(i)
		return dic

	def encode(self):
		dic = self.__initialize_dic(self.__bit)
		out_st = ""
		buffer = ""
		a = len(dic)
		if bytes is str:
			string = self.__input
		else:
			if isinstance(self.__input, bytes):
				string = [chr(b) for b in self.__input]
			else:
				string = [chr(b) for b in bytes(self.__input.encode("UTF-8"))]
		for s in string:
			if buffer+s in dic:
				buffer += s
			else:
				out_st+=dic[buffer]
				if a <= 2**self.__bit:
					dic[buffer+s] = self.__decimal_to_chars(a,self.__bit)
				a += 1
				buffer = s
		out_st+=dic[buffer]
		return out_st

	def __chunks(self,l, n):
		return [l[i:i+n] for i in range(0, len(l), n)]

	def decode(self):
		chunk_size = int(self.__bit/8)
		dic = self.__initialize_rev_dic(self.__bit)
		
		pcode = self.__input[:chunk_size]
		out_st = dic[pcode]
		a = len(dic)
		for ccode in self.__chunks(self.__input[chunk_size:],chunk_size):
			try:
				entry =  dic[ccode]
				out_st += entry
				dic[self.__decimal_to_chars(a,self.__bit)] = dic[pcode]+entry[0]
			except Exception:
				entry = dic[pcode]+dic[pcode][0]
				out_st += entry
				dic[self.__decimal_to_chars(a,self.__bit)] = entry
			a += 1
			pcode = ccode
		return out_st

		

def instance(c,st):
	if c==0:
		return Huffman(st)
	if c==2:
		return LZW(st,16)
	if c==3:
		return LZW(st,24)
	if c==4:
		return LZW(st,32)
	print(c)


def __test():
	s = open('files/pride_and_prejudice.txt').read()
	#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbsaaaaaaaaaaaaaaaaaassaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*1000
	print(len(s))
	enc = LZW(s,16).encode()
	print(len(enc))
	enc = Huffman(enc).encode()
	print(len(enc))
	enc = Huffman(enc).decode()
	print(len(enc))
	enc =LZW(enc,16).decode()
	print(len(enc))
	print(enc==s)




def __main():
	__test()


if __name__=="__main__":
	__main()