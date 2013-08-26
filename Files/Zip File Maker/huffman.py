from collections import defaultdict
from  operator import itemgetter
import sys
import os
from cStringIO import StringIO
import cPickle
import shutil

class Dx:

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

	def initialize_dic(self):
		dic = {}
		for i in range(256):
			dic[chr(i)]=i
		return dic

	def initialize_lst(self):
		dic = []
		for i in range(256):
			dic.insert(i,chr(i))
		return dic

	def LZ78_enc(self,st):
		dic = self.initialize_dic()
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



	def LZ78_dec(self,st):
		dic = self.initialize_lst()
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
				if ccode>len(dic):
					raise Exception("")
				entry = dic[pcode]+dic[pcode][0]
				out_st += entry
				dic.append(entry)
			pcode = ccode
		return out_st


	def __compress_file(self,fi):

		string = ""
		f = open(fi, 'rb')
		while True:
			s = f.read(1)
			if s=='':
				break
			string += s
		f.close()
		name  = fi.split('.')[0]
		zip = self.__huffman_enc(self.LZ78_enc(string))
		out =open(fi+'.dx', 'wb')
		out.write(str(len(zip[1]))+'\n')
		out.write('\n')
		out.write(zip[1]+zip[0])
		out.close
		return fi+'.dx'

	def __decompress_file(self,fi):
		f = open(fi,'rb')	
		size = []
		header = ""
		while True:
			a = f.readline()
			if a=='\n':
				break
			size += [int(a.replace('\n',''))]
		name  = fi[:len(fi)-3]
		data = f.read()
		data = data.replace(header,'')
		f.close()
		string = self.LZ78_dec(self.__huffman_dec((data[size[0]:],data[:size[0]])))
		f = open(name,'wb')
		f.write(string+'\n')
		f.close
		return name

	def __folder_pack(self,fi):
		if not os.path.isfile(fi):
			data_to_write=''
			info = open(fi+".ar",'wb')
			files=os.listdir(fi)
			info.write('<<FOLDER>>\n')
			for fa in files:
				merged_folder = self.__folder_pack(fi+"/"+fa)
				print fi+"/"+fa
				a = open(merged_folder,'rb')
				data = a.read()
				info.write(merged_folder+'\t'+str(len(data))+'\n')
				os.remove(merged_folder)
				data_to_write += data
				a.close()
			info.write('\n')
			info.write(data_to_write)
			info.close()
		else:
			shutil.copy(fi,fi+".ar")		
		return fi+".ar"

	def __folder_unpack(self,fi):
		info = open(fi,'rb')
		if info.readline()=='<<FOLDER>>\n':
			files = []
			while True:
				s = info.readline()
				if s=='\n':
					break
				a = s.split('\t')
				files += [(a[0],int(a[1].replace('\n','')))]
			data = info.read()
			if not os.path.exists(fi[:-3]):
				os.makedirs(fi[:-3])
			total = 0
			for f in files:
				print f[0]
				fa = open(f[0],'wb')
				fa.write(data[total:total+f[1]])
				fa.close()
				total += f[1]
				self.__folder_unpack(f[0])
		os.remove(fi)
		return fi[:-3]

	def compress(self,fi):
		print "Packing..."
		ar = self.__folder_pack(fi)
		print "Packing...Done"
		print "Compressing..."
		out = self.__compress_file(ar)
		os.remove(ar)
		print "Compressing...Done"
		print fi+" size was: {} KB".format(self.__get_size(fi)/1000.0)
		print out+" size is: {} KB".format(self.__get_size(out)/1000.0)
		return out

	def decompress(self,fi):	
		if fi[-2:]!='dx':
			raise Exception("File not compressed")
		print "Decompressing..."
		ar = self.__decompress_file(fi)
		print "Decompressing...Done"
		print "Unpacking..."
		o = self.__folder_unpack(ar)
		print "Unpacking...Done"
		print fi+"size was: {} KB".format(self.__get_size(fi)/1000.0)
		print o+" size is: {} KB".format(self.__get_size(o)/1000.0)
		return o

	
def main(op,fi):
	o = ''
	if op=='-c':
		o = Dx().compress(fi)
	elif op=='-d':
		o = Dx().decompress(fi)

	




if __name__=="__main__":
	main(sys.argv[1],sys.argv[2])