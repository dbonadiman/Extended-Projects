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
		return (self.__bit_to_char("".join([conversion_table[c] for c in st])),ht)

	def __huffman_dec(self,(st,ht)):
		string = ""
		t = ()
		t = ht[0]
		for s in self.__char_to_bit(st):
			if isinstance(t[int(s)][0], tuple):
				t = t[int(s)][0]
			else:
				string += t[int(s)][0]
				t = ht[0]
		return string

	def __find_name(self, name, i):
		out_name = name
		if i>0:
			out_name+='('+str(i)+')'
		if os.path.exists(out_name+".txt"):
   			self.__find_name(name, i+1)
   		else:
   			return out_name
		


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
		if not os.path.exists(name+'.temp'):
			os.makedirs(name+'.temp')
		f = open(name+'.temp/'+name.split('/')[-1]+'.tx','wb')
		f.write(zip[0])
		f.close()
		cPickle.dump(zip[1],open(name+'.temp/'+name.split('/')[-1]+'.ht','wb'))
		files=os.listdir(name+'.temp')
		out =open(self.fi+'.dx', 'wb')
		for f in files:
			out.write(str(os.path.getsize(name+'.temp/'+f))+'\n')
		out.write('\n')
		out.close()
		for f in files:
			data=open(name+'.temp/'+f,"r")
			out=open(self.fi+'.dx', 'a')
			for line in data:
				out.write(line)
			data.close()
			out.close()
		shutil.rmtree(name+'.temp')
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
		if not os.path.exists(name+'.temp'):
			os.makedirs(name+'.temp')
		f = open(name+'.temp/'+name.split('/')[-1]+'.ht','wb')
		f.write(data[:size[0]])
		f.close()
			
		aa = data[size[0]:]
		f.close()
		string = self.__huffman_dec((aa,cPickle.load(open(name+'.temp/'+name.split('/')[-1]+'.ht','rb'))))

		f = open(name,'wb')
		f.write(string+'\n')
		f.close
		shutil.rmtree(name+'.temp')
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
			return out
		else: 
			return Dx(self.fi).__compress_file()

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
			print files
			for f in files:
				print f
				fa = open(f[0],'wb')
				fa.write(data[t:t+f[1]])
				fa.close()
				t += f[1]
				Dx(f[0]).decompress()
				os.remove(f[0])
			os.remove(o)
			o = o[:-2]
		return o







def get_size(start_path = '.'):
	if os.path.isfile(start_path):
		return os.path.getsize(start_path)
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size
	
def main(op,fi):
	o = ''
	if op=='-c':
		o = Dx(fi).compress()
	elif op=='-d':
		o = Dx(fi).decompress()
	print "The file size was: {} KB".format(get_size(fi)/1000.0)
	print "The file size is: {} KB".format(get_size(o)/1000.0)

	




if __name__=="__main__":
	main(sys.argv[1],sys.argv[2])