from collections import defaultdict
from  operator import itemgetter

def ht_from_dic(dic):
	tuples =  dic.items()	
	while len(tuples)>1:
		m = min(tuples, key=itemgetter(1))
		tuples.remove(m)
		n = min(tuples, key=itemgetter(1))
		tuples.remove(n)
		tuples += [((m,n),m[1]+n[1])]
	return tuples[0]

		
def search_in_tree(ht,c):
	if ht == c:
		return ""
	else:
		if isinstance(ht[0], tuple):
			string  =	search_in_tree(ht[0][0],c)
			if string is None:
				string  = search_in_tree(ht[1][0],c)
				if not string is None:
					return "1"+string
			else:
				return "0"+string

def huffman_enc(st):
	dic = defaultdict(int)
	print "Counting"
	for s in st:
		dic[s] += 1
	print "Count Done."
	print "Building Tree"
	ht = ht_from_dic(dic)
	print "Tree Done"
	print "Building Conversion Table"
	chars = set(st)
	conversion_table = {}
	for c in chars:
		bin_str = search_in_tree(ht[0],c)
		print "{} ==> {}".format(c,bin_str)
		conversion_table[c] = bin_str
	print "Conversion Table Done"

	return ("".join([conversion_table[c] for c in st]),ht)

def huffman_dec((st,ht)):
	string = ""
	t = ()
	t = ht[0]
	for s in st:
		if isinstance(t[int(s)][0], tuple):
			t = t[int(s)][0]
		else:
			string += t[int(s)][0]
			t = ht[0]
	return string


def decimal_to_binary(num):
	binary = ""
	while num>0:
		binary+=str(num%2)
		num = num/2
	return binary[::-1] #this reverse the string

def main():
	string = ""
	f = open('divina_commedia.txt', 'r')
	while True:
		s = f.readline()
		if s=='':
			break
		string += s
	zip = huffman_enc(string)
	print "The text size was: "+str(len("".join([decimal_to_binary(ord(c)) for c in string]))/8)+" byte"
	print "The text compressed size is: "+str(len(zip[0])/8)+" byte"
	decripted = huffman_dec(zip)
	print decripted
	if string==decripted:
		print True
	else:
		print False


if __name__=="__main__":
	main()