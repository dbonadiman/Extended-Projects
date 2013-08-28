import sys
import os
import encoding
import shutil


def __compress_file(fi,fo,args):
	f = open(fi, 'rb')
	st = f.read()
	f.close()
	for arg in args:
		print encoding.instance(arg,st)
		st = encoding.instance(arg,st).encode()
	out =open(fo, 'wb')
	out.write(st)
	out.close()
	return fo


def __decompress_file(fi,fo,args):
	f = open(fi,'rb')	
	st = f.read()
	f.close()
	for arg in args:
		print encoding.instance(arg,st)
		st = encoding.instance(arg,st).decode()
	f = open(fo,'wb')
	f.write(st+'\n')
	f.close
	return fo

def __folder_pack(fi,fo):
	if not os.path.isfile(fi):
		data_to_write=''
		info = open(fo,'wb')
		files=os.listdir(fi)
		info.write('<<FOLDER>>\n')
		for fa in files:
			merged_folder = __folder_pack(fi+"/"+fa,fi+"/"+fa+'.temp')
			a = open(merged_folder,'rb')
			data = a.read()
			info.write(merged_folder+'\t'+str(len(data))+'\n')
			info.write(data)
			a.close()
			os.remove(merged_folder)
		info.write('\n')
		info.close()
	else:
		shutil.copy(fi,fo)
	print fi		
	return fo

def __folder_unpack(fi,fo):
	info = open(fi,'rb')
	if info.readline()=='<<FOLDER>>\n':
		files = []
		if not os.path.exists(fo):
			os.makedirs(fo)
		while True:
			s = info.readline()
			if s=='\n':
				break
			a = s.split('\t')
			f = (a[0],int(a[1].replace('\n','')))
			data = info.read(f[1])
			fa = open(f[0],'wb')
			fa.write(data)
			fa.close()
			__folder_unpack(f[0],f[0][:-4])	
	os.remove(fi)
	print fo
	return fo

def compress(fi,fo,pipeline=[encoding.LZW24,encoding.HUFFMAN]):
	print "Packing...\n"
	ar = __folder_pack(fi,fi+'.temp')
	print "Packing...Done\n"
	print "Compressing...\n"
	out = __compress_file(ar,fo,pipeline)
	os.remove(ar)
	print "Compressing...Done\n"
	return out

def decompress(fi,fo,pipeline=[encoding.LZW24,encoding.HUFFMAN]):	
	print "Decompressing...\n"
	ar = __decompress_file(fi,fi+'.temp',pipeline[::-1])
	print "Decompressing...Done\n"
	print "Unpacking...\n"
	out = __folder_unpack(ar,fo)
	print "Unpacking...Done\n"
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