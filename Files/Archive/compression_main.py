import sys
import os
import compression 
import shutil

def __compress_file(fi,fo,codec="DEFLATE"):
    f = open(fi, 'rb')
    st = f.read()
    f.close()
    st = compression.encode(st,codec)
    out =open(fo, 'wb')
    out.write(st)
    out.close()
    return fo

def __decompress_file(fi,fo,codec="DEFLATE"):
    f = open(fi,'rb')    
    st = f.read()
    f.close()
    st = compression.decode(st,codec)
    f = open(fo,'wb')
    f.write(st)
    f.close
    return fo

def __folder_pack(fi,fo):
    if not os.path.isfile(fi):
        data_to_write=''
        info = open(fo,'wb')
        files=os.listdir(fi)
        info.write('<<FOLDER>>\n'.encode('utf-8'))
        for fa in files:
            merged_folder = __folder_pack(fi+"/"+fa,fi+"/"+fa+'.temp')
            a = open(merged_folder,'rb')
            data = a.read()
            a.close()
            info.write('{}\t{}\n'.format(merged_folder,len(bytearray(data))).encode('utf-8'))
            info.write(bytearray(data))
            os.remove(merged_folder)
        info.write('\n'.encode('utf-8'))
        info.close()
    else:
        shutil.copy(fi,fo)
    print(fi)        
    return fo

def __folder_unpack(fi,fo):
    info = open(fi,'rb')
    if info.readline()=='<<FOLDER>>\n'.encode('utf-8'):
        files = []
        if not os.path.exists(fo):
            os.makedirs(fo)
        while True:
            s = info.readline().decode('utf-8')
            if s=='\n':
                break
            a = s.split('\t')
            try:
                f = (a[0],int(a[1].replace('\n','')))
            except Exception:
                raise Exception()
            data = info.read(f[1])
            fa = open(f[0].replace('\0',''),'wb')
            fa.write(data)
            fa.close()
            __folder_unpack(f[0].replace('\0',''),f[0][:-5].replace('\0',''))    
    else:
        shutil.copy(fi,fo)
    os.remove(fi)
    print(fo)
    return fo

def compress(fi,fo,codec=None):
    if codec is None:
        codec = "DEFLATE"
    print("Packing...\n")
    ar = __folder_pack(fi,fi+'.temp')
    print("Packing...Done\n")
    print("Compressing...\n")
    out = __compress_file(ar,fo,codec)
    os.remove(ar)
    print("Compressing...Done\n")
    return out

def decompress(fi,fo,codec=None):
    if codec is None:
        codec = "DEFLATE"
    print("Decompressing...\n")
    ar = __decompress_file(fi,fi+'.temp',codec)
    print("Decompressing...Done\n")
    print("Unpacking...\n")
    out = __folder_unpack(ar,fo)
    print("Unpacking...Done\n")
    return out

def __test():
    try:
        compress('files','files.co')
        decompress('files.co','files')
    except Exception():
        print("Failed!!")
    else:
        print("Success")
    
def __main(op,fi):
    if op=='-c':
        compress(fi,fi+'.co')
    if op=='-d':
        decompress(fi,fi[:-3])

if __name__=="__main__":
        if len(sys.argv)==3:
            __main(sys.argv[1],sys.argv[2])
        else:
            __test()
