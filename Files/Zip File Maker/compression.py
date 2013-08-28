import sys
import os
import encoding
import shutil
import math
import cPickle
import zipfile

def zipdir(fi, fo):
	zip = zipfile.ZipFile(fo, 'w', zipfile.ZIP_DEFLATED))
	for root, dirs, files in os.walk(fi):
		for file in files:
			zip.write(os.path.join(root, file))
	zip.close()


def __h(files):
  data = ""
  if os.path.isfile(files):
  	data = open(files,'rb').read()
  else:
  	o=os.listdir(files)
  	for f in o:
  		data += open(files+'/'+f,'rb').read()
  if not data:
    return 0
  entropy = 0
  for x in range(256):
    p_x = float(data.count(chr(x)))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
  return entropy

def __get_size(start_path = '.'):
	if os.path.isfile(start_path):
		return os.path.getsize(start_path)
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size




def __compress_file(fi,fo):
	f = open(fi, 'rb')
	string = f.read()
	f.close()
	name  = fi.split('.')[0]
	enc = encoding.LZ78_enc(string)
	zip = encoding.huffman_enc(enc)
	out =open(fo, 'wb')
	if isinstance(zip,tuple):
		tmp = cPickle.dumps(zip[1])
		out.write(str(len(tmp))+"\n")
		out.write(str(zip[2])+"\n")
		out.write(tmp)
		out.write(zip[0])
	else:
		out.write(zip)
	out.close()
	return fo


def __decompress_file(fi):
	f = open(fi,'rb')	
	name  = fi[:-3]
	data = f.readline()
	try:
		size = int(data)
		d2 = f.readline() 
		leng = int(d2)
		data += d2
	except Exception, e:
		data += f.read()
	else:
		data = f.read()
		data = (data[size:],cPickle.loads(data[:size]),leng)
	f.close()
	enc = encoding.huffman_dec(data)
	string = encoding.LZ78_dec(enc)
	f = open(name,'wb')
	f.write(string+'\n')
	f.close
	return name

def __folder_pack(fi):
	if not os.path.isfile(fi):
		data_to_write=''
		info = open(fi+".ar",'wb')
		files=os.listdir(fi)
		info.write('<<FOLDER>>\n')
		for fa in files:
			merged_folder = __folder_pack(fi+"/"+fa)
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

def __folder_unpack(fi,fo):
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
		if not os.path.exists(fo):
			os.makedirs(fo)
		total = 0
		for f in files:
			print f[0][:-3]
			fa = open(f[0],'wb')
			fa.write(data[total:total+f[1]])
			fa.close()
			total += f[1]
			__folder_unpack(f[0],f[0][:-3])
	os.remove(fi)
	return fo

def compress(fi,fo):
	print "Packing..."
	ar = __folder_pack(fi)
	print "Packing...Done"
	print "Compressing..."
	out = __compress_file(ar,fo)
	os.remove(ar)
	print "Compressing...Done"
	print "Zip"
	zipdir(fi,fi+".zip")
	print fi+" size was: {} KB and the entryopy:  {}".format(__get_size(fi)/1000.0,__h(fi))
	print out+" size is: {} KB and the entryopy:  {}".format(__get_size(out)/1000.0,__h(out))
	print fi+".zip size is: {} KB and the entryopy:  {}".format(__get_size(fi+".zip")/1000.0,__h(fi+".zip"))
	return out

def decompress(fi,fo):	
	print "Decompressing..."
	ar = __decompress_file(fi)
	print "Decompressing...Done"
	print "Unpacking..."
	out = __folder_unpack(ar,fo)
	print "Unpacking...Done"
	print fi+" size was: {} KB and the entryopy:  {}".format(__get_size(fi)/1000.0,__h(fi))
	print out+" size is: {} KB and the entryopy:  {}".format(__get_size(out)/1000.0,__h(out))
	return out

	
def __main(op,fi,fo):
	if op=='-c':
		compress(fi,fo)
	if op=='-d':
		decompress(fi,fo)



if __name__=="__main__":
	try:
		__main(sys.argv[1],sys.argv[2],sys.argv[3])
	except Exception, e:
		__main('-c','files','files.compress')
		__main('-d','files.compress','files')