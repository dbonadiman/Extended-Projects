from collections import defaultdict
import cPickle
from cStringIO import StringIO
from  operator import itemgetter

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
	while len(tuples)>1:
		m = min(tuples, key=itemgetter(1))
		tuples.remove(m)
		n = min(tuples, key=itemgetter(1))
		tuples.remove(n)
		tuples += [((m,n),m[1]+n[1])]
	return tuples[0]

def __search_in_tree(ht,c):
	if ht == c:
		return ""
	else:
		if isinstance(ht[0], tuple):
			string  =	__search_in_tree(ht[0][0],c)
			if string is None:
				string  = __search_in_tree(ht[1][0],c)
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

def huffman_enc(st): 
	dic = defaultdict(int)
	for s in st:
		dic[s] += 1
	p="(((((((S'4'\nI963137\nt(S'3'\nI1018943\nttI1982080\nt(((S'2'\nI1175195\nt(S'1'\nI1556659\nttI2731854\nttI4713934\nt(((((S','\nI1677553\nt(((S'0'\nI832167\nt(S'8'\nI860447\nttI1692614\nttI3370167\nt(((((S'7'\nI860586\nt(S'9'\nI864030\nttI1724616\nt(((S'6'\nI875414\nt(S'5'\nI909016\nttI1784430\nttI3509046\nttI6879213\nttI11593147\ntp1\n."
	ht = cPickle.loads(p)

	chars = set(st)
	conversion_table = {}
	for c in chars:
		bin_str = __search_in_tree(ht[0],c)
		conversion_table[c] = bin_str
	return __bit_to_char("".join([conversion_table[c] for c in st]))

def huffman_dec(st):
	string = ""
	p="(((((((S'4'\nI963137\nt(S'3'\nI1018943\nttI1982080\nt(((S'2'\nI1175195\nt(S'1'\nI1556659\nttI2731854\nttI4713934\nt(((((S','\nI1677553\nt(((S'0'\nI832167\nt(S'8'\nI860447\nttI1692614\nttI3370167\nt(((((S'7'\nI860586\nt(S'9'\nI864030\nttI1724616\nt(((S'6'\nI875414\nt(S'5'\nI909016\nttI1784430\nttI3509046\nttI6879213\nttI11593147\ntp1\n."
	ht = cPickle.loads(p)
	t = ()
	t = ht[0]
	for s in __char_to_bit(st):
		if isinstance(t[int(s)][0], tuple):
			t = t[int(s)][0]
		else:
			string += t[int(s)][0]
			t = ht[0]
	return string


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