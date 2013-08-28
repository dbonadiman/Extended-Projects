import cPickle
from cStringIO import StringIO
from  operator import itemgetter


def __bit_to_char(bit_str):
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

def __char_to_bit(string):
	out = ''
	for c in string:
		out += '{0:08b}'.format(ord(c))
	return out

def __ht_from_st(st):
	chars = set(st)
	tuples = [(c,st.count(c)) for c in chars]
	while len(tuples)>1:
		m = min(tuples, key=itemgetter(1))
		tuples.remove(m)
		n = min(tuples, key=itemgetter(1))
		tuples.remove(n)
		tuples += [((m,n),m[1]+n[1])]
	return __remove_count(tuples[0])

def __remove_count((a,b)):
	if isinstance(a,tuple):
		return (__remove_count(a[0]),__remove_count(a[1]))
	else:
		return (a)


def __traverse(ht,s=""):
	if not isinstance(ht,tuple):
		return {ht:s}
	else:
		d1 = __traverse(ht[0],s+'0')
		d1.update(__traverse(ht[1],s+'1'))
		return d1

def __initialize_dic():
	dic = {}
	for i in range(256):
		dic[chr(i)]=i
	return dic

def __initialize_lst():
	dic = []
	for i in range(256):
		dic.insert(i,chr(i))
	return dic

def huffman_enc(st):
	ht = __ht_from_st(st)
	conversion_table = __traverse(ht)
	s = "".join([conversion_table[c] for c in st])
	b =__bit_to_char(s)	
	return (b,ht,len(st))

def huffman_dec(data):
	string =""
	t = data[1]
	for s in __char_to_bit(data[0]):
		if isinstance(t[int(s)], tuple):
			t = t[int(s)]
		else:
			string += t[int(s)]
			t = data[1]
	return string[:data[2]]


def LZ78_enc(st):
	dic = __initialize_dic()
	out_st = ""
	buffer = ""
	a = len(dic)
	for s in st:
		if buffer+s in dic:
			buffer += s
		else:
			out_st+=str(dic[buffer])+","
			dic[buffer+s] = a 
			a += 1
			buffer = s
	out_st+=str(dic[buffer])
	return out_st



def LZ78_dec(st):
	dic = __initialize_lst()
	codes = [int(s)  for s in st.split(',') if s!='']
	pcode = codes[0]
	out_st = dic[pcode]
	for i in range(1,len(codes)):
		ccode = codes[i]
		try:
			entry =  dic[ccode]
			out_st += entry
			dic.append(dic[pcode]+entry[0])
		except Exception, e:
			entry = dic[pcode]+dic[pcode][0]
			out_st += entry
			dic.append(entry)
		pcode = ccode
	return out_st

def __test():
	st = "Ciao come va?"
	enc = huffman_enc(st)
	print enc
	dec = huffman_dec(enc)
	print dec

def __bm():
	st = open('files/divina_commedia.txt').read()
	enc = huffman_enc(st)
	dec = huffman_dec(enc)


def __main():
	__bm()



if __name__=="__main__":
	__main()