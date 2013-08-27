import sys
import os
import encoding
import shutil
import math

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



			

	def __decimal_to_binary(self,num):
		binary = ""
		while num>0:
			binary+=str(num%2)
			num = num/2
		return binary[::-1] #this reverse the string




	def __compress_file(self,fi):
		f = open(fi, 'rb')
		string = f.read()
		f.close()
		name  = fi.split('.')[0]
		zip = encoding.huffman_enc(encoding.LZ78_enc(string))
		out =open(fi+'.dx', 'wb')
		out.write(zip)
		out.close
		return fi+'.dx'

	def __decompress_file(self,fi):
		f = open(fi,'rb')	
		name  = fi[:len(fi)-3]
		data = f.read()
		f.close()
		string = encoding.LZ78_dec(encoding.huffman_dec(data))
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
		print fi+" size was: {} KB and the entryopy:  {}".format(self.__get_size(fi)/1000.0,H(open(fi,'rb').read()))
		print out+" size is: {} KB and the entryopy:  {}".format(self.__get_size(out)/1000.0,H(open(out,'rb').read()))
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



def H(data):
  if not data:
    return 0
  entropy = 0
  for x in range(256):
    p_x = float(data.count(chr(x)))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
  return entropy
	
def main(op,fi):
	if op=='-c':
		Dx().compress(fi)
	if op=='-d':
		Dx().decompress(fi)

	




if __name__=="__main__":
	try:
		main(sys.argv[1],sys.argv[2])
	except Exception, e:
		main('-c',sys.argv[0])