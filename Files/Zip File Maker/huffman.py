from collections import defaultdict
from  operator import itemgetter
import sys
import os
from cStringIO import StringIO
import cPickle
import shutil

class Dx:
	fi = ''
	def __init__(self,fi):
		self.fi = fi

	def __get_size(self,start_path = '.'):
		if os.path.isfile(start_path):
			return os.path.getsize(start_path)
		total_size = 0
		for dirpath, dirnames, filenames in os.walk(start_path):
			for f in filenames:
				fp = os.path.join(dirpath, f)
				total_size += os.path.getsize(fp)
		return total_size

	def __bit_to_char(self,bit_str):
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

	def __char_to_bit(self,string):
		f = StringIO(string)
		aa = ''
		while 1:
			c = f.read(1)
			if not c:
				break
			aa += '{0:08b}'.format(ord(c))
		return aa

	def __ht_from_dic(self,dic):
		tuples =  dic.items()	
		while len(tuples)>1:
			m = min(tuples, key=itemgetter(1))
			tuples.remove(m)
			n = min(tuples, key=itemgetter(1))
			tuples.remove(n)
			tuples += [((m,n),m[1]+n[1])]
		return tuples[0]

			
	def __search_in_tree(self,ht,c):
		if ht == c:
			return ""
		else:
			if isinstance(ht[0], tuple):
				string  =	self.__search_in_tree(ht[0][0],c)
				if string is None:
					string  = self.__search_in_tree(ht[1][0],c)
					if not string is None:
						return "1"+string
				else:
					return "0"+string

	def __decimal_to_binary(self,num):
		binary = ""
		while num>0:
			binary+=str(num%2)
			num = num/2
		return binary[::-1] #this reverse the string

	def __huffman_enc(self,st):
		dic = defaultdict(int)
		for s in st:
			dic[s] += 1
		ht = self.__ht_from_dic(dic)
		chars = set(st)
		conversion_table = {}
		for c in chars:
			bin_str = self.__search_in_tree(ht[0],c)
			conversion_table[c] = bin_str
		return (self.__bit_to_char("".join([conversion_table[c] for c in st])),cPickle.dumps(ht))

	def __huffman_dec(self,(st,p)):
		string = ""
		ht = cPickle.loads(p)
		t = ()
		t = ht[0]
		for s in self.__char_to_bit(st):
			if isinstance(t[int(s)][0], tuple):
				t = t[int(s)][0]
			else:
				string += t[int(s)][0]
				t = ht[0]
		return string

	def __compress_file(self):
		string = ""
		f = open(self.fi, 'rb')
		while True:
			s = f.read(1)
			if s=='':
				break
			string += s
		f.close()
		name  = self.fi.split('.')[0]
		zip = self.__huffman_enc(string)
		out =open(self.fi+'.dx', 'wb')
		out.write(str(len(zip[1]))+'\n')
		out.write('\n')
		out.write(zip[1]+zip[0])
		out.close
		return self.fi+'.dx'

	def __decompress_file(self):
		f = open(self.fi,'rb')	
		size = []
		header = ""
		while True:
			a = f.readline()
			if a=='\n':
				break
			size += [int(a.replace('\n',''))]
		name  = self.fi[:len(self.fi)-3]
		data = f.read()
		data = data.replace(header,'')
		f.close()
		string = self.__huffman_dec((data[size[0]:],data[:size[0]]))
		f = open(name,'wb')
		f.write(string+'\n')
		f.close
		return name

	def compress(self):		
		if not os.path.isfile(self.fi):
			f = open(self.fi+"_c",'wb')
			info = open(self.fi+".f",'wb')
			files=os.listdir(self.fi)
			info.write('<<FOLDER>>\n')
			for fa in files:
				o = Dx(self.fi+"/"+fa).compress()
				a = open(o,'rb')
				info.write(o+'\t'+str(os.path.getsize(o))+'\n')
				os.remove(o)
				f.write(a.read())
				a.close()
			info.write('\n')
			f.close()
			f = open(self.fi+"_c",'rb')
			info.write(f.read())

			f.close()
			info.close()
			out = Dx(self.fi+".f").compress()
			os.remove(self.fi+"_c")
			os.remove(self.fi+".f")
			#os.rename(out,out.replace('.f',''))
			print self.fi+" size was: {} KB".format(self.get_size(self.fi)/1000.0)
			print out+" size is: {} KB".format(self.get_size(out)/1000.0)
			return out
		else: 
			o = Dx(self.fi).__compress_file()
			print self.fi+" size was: {} KB".format(self.get_size(self.fi)/1000.0)
			print o+" size is: {} KB".format(self.get_size(o)/1000.0)
			return o

	def decompress(self):
		
		if self.fi[-2:]!='dx':
			raise Exception("File not compressed")
		o = Dx(self.fi).__decompress_file()
		info = open(o,'rb')
		if info.readline()=='<<FOLDER>>\n':
			files = []
			while True:
				s = info.readline()
				if s=='\n':
					break
				a = s.split('\t')
				files += [(a[0],int(a[1].replace('\n','')))]
			data = info.read()
			if not os.path.exists(o[:-2]):
				os.makedirs(o[:-2])
			t = 0
			for f in files:
				fa = open(f[0],'wb')
				fa.write(data[t:t+f[1]])
				fa.close()
				t += f[1]
				Dx(f[0]).decompress()
				os.remove(f[0])
			os.remove(o)
			o = o[:-2]
		print self.fi+"size was: {} KB".format(self.get_size(self.fi)/1000.0)
		print o+" size is: {} KB".format(self.get_size(o)/1000.0)
		return o








	
def main(op,fi):
	o = ''
	if op=='-c':
		o = Dx(fi).compress()
	elif op=='-d':
		o = Dx(fi).decompress()

	




if __name__=="__main__":
	main(sys.argv[1],sys.argv[2])