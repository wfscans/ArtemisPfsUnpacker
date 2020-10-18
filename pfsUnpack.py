#port of the below to python3
#https://github.com/Azukee/Macaron/blob/master/ArchiveUnpacker.Unpackers/Unpackers/ArtemisUnpacker.cs

import hashlib
import struct
import os
import sys

def int32(s):
 return struct.unpack('i', s)[0]

def processArchive (aname):
 print(aname)
 with open(aname, 'rb') as f:
  if f.read(2) != b"pf":
   raise Exception("Not an Artemis pfs archive!")
  version = int(f.read(1))
  headLen = int32(f.read(4))
  shakey = hashlib.sha1(f.read(headLen)).digest()
  print("shakey", shakey.hex())
  f.seek(-headLen, 1)
  files = int32(f.read(4)) #file count. Just inline?
  print(files-1,"files")
  curpos = 0
  for file in range(0, files):
   filepath = aname.replace(".","") + "/" + f.read(int32(f.read(4))).decode().replace("\\","/")
   f.seek(4, 1)
   offset = int32(f.read(4))
   size  = int32(f.read(4))
   os.makedirs(os.path.dirname(filepath), exist_ok=True)
   print(file, filepath)
   with open(filepath, 'wb') as fo:
    if version == 8:
     curpos = f.tell()
     f.seek(offset)
     for i in range(0, size+1, 20): #increment by length of sha key(in bytes)
      buf = bytearray(f.read(min(size-i, 20)))
      for j in range(0, len(buf)):
       buf[j] ^= shakey[j]
      fo.write(buf)
   #else:
    #do something (FileSlice)
   f.seek(curpos) #go back to the header table

if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("You did something wrong. Output will be in current directory. Ex. pfsUnpack.py root.pfs")
 else:
  processArchive(sys.argv[1])
