from collections import defaultdict
import cPickle
from cStringIO import StringIO
from  operator import itemgetter

DEFAULT_HT=""

def __bit_to_char(bit_str):
	sio = StringIO(bit_str)
	out = StringIO()
	while 1:
		b = sio.read(8)
		if not b:
			break
		if len(b) < 8:
			b = b + '0' * (8 - len(b))
		i = int(b, 2)
		c = chr(i)
		out.write(c)
	output = out.getvalue()
	out.close()
	return output

def __char_to_bit(string):
	f = StringIO(string)
	aa = ''
	while 1:
		c = f.read(1)
		if not c:
			break
		aa += '{0:08b}'.format(ord(c))
	return aa

def __ht_from_dic(dic):
	tuples =  dic.items()
	tuples += [('\0',0)]
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


def __search_in_tree(ht,c):
	if ht == c:
		return ""
	else:
		if isinstance(ht, tuple):
			string  =	__search_in_tree(ht[0],c)
			if string is None:
				string  = __search_in_tree(ht[1],c)
				if not string is None:
					return "1"+string
			else:
				return "0"+string

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

def huffman_enc(st,create_ht = False): 
	if create_ht:
		dic = defaultdict(int)
		for s in st:
			dic[s] += 1
		ht = __ht_from_dic(dic)
	else:
		ht = cPickle.loads(DEFAULT_HT)
	chars = set(st)
	conversion_table = {}
	for c in chars:
		bin_str = __search_in_tree(ht,c)
		conversion_table[c] = bin_str
	if create_ht:
		b ="".join([conversion_table[c] for c in st])
		return (__bit_to_char(b),cPickle.dumps(ht))
	return __bit_to_char("".join([conversion_table[c] for c in st]))

def huffman_dec(st):
	string = ""
	if not isinstance(st,tuple):
		ht = cPickle.loads(DEFAULT_HT)
	else:
		ht = cPickle.loads(st[1])
		st = st[0]
	t = ()
	t = ht
	for s in __char_to_bit(st):
		if isinstance(t[int(s)], tuple):
			t = t[int(s)]
		else:
			string += t[int(s)]
			t = ht
	return string.replace('\0','')


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

def __main():
	st = open('files/divina_commedia.txt').read()
	enc = huffman_enc(st,True)
	dec = huffman_dec(enc)
	print dec == st



if __name__=="__main__":
	__main()