import os, sys, getpass as gps, collections as clc
import addendum as a, cypherGram as cpg, guhyamu as guh

# AUTHENTICATE USER

# PREPARE ENV
kiSet=[]
mapKey=0
keyMapper=clc.OrderedDict()
os.chdir(a.apath('bin'))
binFiles=a.g.glob('*')
for fil in binFiles:
    keyMapper[mapKey]=fil
    kiSet.append(open(fil).read().encode().splitlines())
    mapKey+=1

def krypto(s):
 global keyMapper,kiSet
 xx=a.r.randint(0,len(kiSet)-1)
 fiKey=keyMapper[xx]
 myKey=kiSet[xx][a.r.randint(0,len(kiSet[xx])-1)]
 krypo=guh.guhya(cpg.cypher(fiKey,s,myKey))
 return krypo

def dkrypto(s):
 global keyMapper,kiSet
 sti=guh.niguhya(s)
 fiKey=sti[:2]+sti[-2:]
 fiKey=fiKey[-1]+fiKey[:2][::-1]+fiKey[2:3]
 for i in range(len(kiSet)):
  if(keyMapper[i]==fiKey):
   key=i
   break
  continue
#  18001037799
 dkryo=cpg.deCypher(sti,kiSet[key])
 return dkryo

def fiOps(o,a,z):
 global keyMapper,kiSet
 inSet=list(open(a).read().splitlines())
 oSet=[]
 if(o==1):
  oSet=[krypto(li) for li in inSet]
 elif(o==3):
  oSet=[dkrypto(li) for li in inSet]
 else:
  print('Invalid Medium')
 with open(z,'w') as thisFile:
  for item in oSet:
   thisFile.write("{}\n".format(item))
 return

while(1):
 os.system('clear')
 print('\nk-Kryptobits welcomes you')
 print('\t\t\t Kbits Customized encryption')
 print('\n0. Quit\n1. KRYPT O FILE\n2. KRYPT O STRING\n3. DKRYPT O FILE\n4. DKRYPT O STRING')
 print('\nSELECT OPTION : ')
 opt=int(input())
 if(opt==0):
  kiSet=[]
  sys.exit()
 if(opt==1 or opt==3):
  print('Input Filename : ')
  fin=str(input())
  print('Out Filename : ')
  fop=str(input())
  fiOps(opt,fin,fop)
 elif(opt==2):
  print('Input String : ')
  key = str(input())
  print(krypto(key))
 elif(opt==4):
  print('Input String : ')
  key = str(input())
  print(dkrypto(key))
 elif(opt==9):
  print(keyMapper)
  print([len(kset) for kset in kiSet])
  print(kiSet[1][14])
 else:
  print('Invalid option')
 input('\nPress Enter to continue ...')
