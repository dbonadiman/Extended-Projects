from cStringIO import StringIO


HUFFMAN = 0
LZW12 = 1
LZW16 = 2


class Huffman(object):

	__input =""

	def __init__(self,data):
		self.__input=data

	def __bit_to_char(self,bit_str):
		sio = StringIO(bit_str)
		out = ""
		while 1:
			b = sio.read(8)
			if not b:
				break
			if len(b) < 8:
				b = b + '0' * (8 - len(b))
			out+=chr(int(b, 2))
		return out

	def __char_to_bit(self,string):
		out = ''
		for c in string:
			out += '{0:08b}'.format(ord(c))
		return out

	def __dump_data(self,data):
		import cPickle

		out =StringIO()
		tmp = cPickle.dumps(data[1])
		out.write(str(len(tmp))+"\n")
		out.write(str(data[0])+"\n")
		out.write(tmp)
		out.write(data[2])
		re = out.getvalue()
		out.close()
		return re


	def __loads_data(self,st):
		import cPickle

		f = StringIO(st)
		data = f.readline()
		size = int(data)
		d2 = f.readline() 
		leng = int(d2)
		data = f.read()
		return(leng,cPickle.loads(data[:size]),data[size:])



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

	def __remove_count(self,(a,b)):
		if isinstance(a,tuple):
			return (self.__remove_count(a[0]),self.__remove_count(a[1]))
		else:
			return (a)

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
	__bit = 0

	def __init__(self,data,bit=12):
		self.__input=data
		self.__bit=bit

	def __bit_to_char(self,bit_str):
		sio = StringIO(bit_str)
		out = ""
		while 1:
			b = sio.read(8)
			if not b:
				break
			if len(b) < 8:
				b = b + '0' * (8 - len(b))
			out+=chr(int(b, 2))
		return out

	def __char_to_bit(self,string):
		out = ''
		for c in string:
			out += '{0:08b}'.format(ord(c))
		return out

	def __decimal_to_binary(self, num, bit):
		binary = ""
		while num>0:
			binary+=str(num%2)
			num = num/2
		if len(binary) < bit:
			binary += str(0)*(bit-len(binary))
		return binary[::-1]

	def __initialize_dic(self,bit):
		dic = {}
		for i in range(256):
			dic[chr(i)]=self.__decimal_to_binary(i,bit)
		return dic

	def __initialize_rev_dic(self,bit):
		dic = {}
		for i in range(256):
			dic[self.__decimal_to_binary(i,bit)]=chr(i)
		return dic

	def encode(self):
		dic = self.__initialize_dic(self.__bit)
		out_st = ""
		buffer = ""
		a = len(dic)
		for s in self.__input:
			if buffer+s in dic:
				buffer += s
			else:
				out_st+=str(dic[buffer])
				if a <= 2**self.__bit:
					dic[buffer+s] = self.__decimal_to_binary(a,self.__bit)
				a += 1
				buffer = s
		out_st+=str(dic[buffer])
		return self.__bit_to_char(out_st)



	def decode(self):
		dic = self.__initialize_rev_dic(self.__bit)
		sio = StringIO(self.__char_to_bit(self.__input))
		pcode = sio.read(self.__bit)
		out_st = dic[pcode]
		a = len(dic)
		while 1:
			ccode = sio.read(self.__bit)
			if not ccode:
				break

			try:
				entry =  dic[ccode]
				out_st += entry
				dic[self.__decimal_to_binary(a,self.__bit)] = dic[pcode]+entry[0]

			except Exception, e:
				entry = dic[pcode]+dic[pcode][0]
				out_st += entry
				dic[self.__decimal_to_binary(a,self.__bit)] = entry
			a += 1
			pcode = ccode
		return out_st

		

def instance(c,st):
	if c==0:
		return Huffman(st)
	if c==1:
		return LZW(st)
	if c==2:
		return LZW(st,16)
	print c


def __test():
	enc = open('files/divina_commedia.txt').read()
	print len(enc)
	enc = LZW(enc).encode()
	print len(enc)
	enc = Huffman(enc).encode()
	print len(enc)
	enc = Huffman(enc).decode()
	print len(enc)
	enc = LZW(enc).decode()
	print len(enc)



def __main():
	__test()




if __name__=="__main__":
	__main()