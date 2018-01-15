import os, addendum as a

def kfile():
 files=os.listdir(a.apath('lib'))
 kFile=a.apath('lib')+files[a.r.randint(0,len(files)-1)]
 return kFile

def guhya(gst):
 kfi=kfile()
 lines=a.sbp.check_output(['wc','-l', kfi])
 lines=int([int(s) for s in lines.split() if s.isdigit()][0])
 key=a.lnc.getline(kfi,a.r.randint(0,lines)).split()
 gid=a.lnc.getline(kfi,1)
 gid=gid[:-1]
 dicto=key[0]
 diKey=key[1]
 kKey=a.r.randint(101,999)
 guhStr=''
 for c in gst:
  idx=dicto.index(c)
  sidx=(idx+kKey)%len(dicto)
  guhStr+=dicto[sidx]
 kKey=str(kKey)
 guhst=guhStr[:14][::-1]+kKey[:1]+diKey[16:][::-1]+gid[:12]+guhStr[14:-2]+gid[12:][::-1]+diKey[:16]+guhStr[-2:][::-1]+kKey[::-1][:2]
 return guhst

def niguhya(gst):
 ens=''
 kKey=gst[14:15]
 kKey+=gst[::-1][:2]
 kKey=int(kKey)
 diKey=gst[-20:-4]+gst[15:31][::-1]
 gido=gst[31:43]+gst[-32:-20][::-1]
 gst=gst[:14][::-1]+gst[43:-32]+gst[-4:-2][::-1]
 files=os.listdir(a.apath('lib'))
 for kfi in files:
  lines=a.sbp.check_output(['wc','-l', a.apath('lib')+kfi])
  lines=int([int(s) for s in lines.split() if s.isdigit()][0])
  key=a.lnc.getline(a.apath('lib')+kfi,a.r.randint(0,lines)).split()
  gid=a.lnc.getline(a.apath('lib')+kfi,1)
  gid=gid[:-1]
  if(gid!=gido):
   continue
  with open(a.apath('lib')+kfi) as myFile:
   for num, line in enumerate(myFile, 1):
    if diKey in line:
     line=line.split()
     dicto=line[0]
     break
  break
 for c in gst:
  idx=dicto.index(c)
  sidx=(idx-kKey)%len(dicto)
  ens+=dicto[sidx]
 return ens
