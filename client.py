import os, addendum as a, linecache as lnc, subprocess as sp

os.system('clear')
cfile='/migrations/bin/key.bin'
lines = sp.check_output(['wc','-l', cfile])
lines = int([int(s) for s in lines.split() if s.isdigit()][0])

def krypto(s):
 global cfile, lines
 key=bytes(lnc.getline(cfile,a.r.randint(0,lines)))
 return key


#PRIME
print('\nk-Kryptobits welcomes you')
print('\t\t\t Kbits Customized encryption')
print('\n1. KRYPT O FILE\n2. KRYPT O STRING\n3. DKRYPT O FILE\n4. DKRYPT O STRING')
print('\nSELECT OPTION : ')
opt=int(input())
if(opt==1 or opt==3):
 print('Input Filename : ')
 fin=str(input())
 print('Out Filename : ')
 fop=str(input())
 fileops(opt,fin,fop)
elif(opt==2):
 print('Input String : ')
 key = str(input())
 print(krypto(key))
elif(opt==4):
 print('Input String : ')
 key = str(input())
 print(decrypt(key))
else:
 print('Invalid option')

