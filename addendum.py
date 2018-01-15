import re, string as stg, random as r, uuid as uid, subprocess as sbp, linecache as lnc, glob as g

c=stg.ascii_letters
x=stg.digits
a=c+x

def apath(l='app'):
    app='/app/kryptobits/'
    if(l=='lib'):
        app='/app/kryptobits/lib/'
    elif(l=='wsp'):
        app='/app/kryptobits/wsp/'
    elif(l=='bin'):
        app='/app/kryptobits/bin/'
    return app

def cdum(n=8):
 global c
 return ''.join(r.choice(c) for _ in range(n))

def ndum(n=8):
 global x
 return ''.join(r.choice(x) for _ in range(n))

def adum(n=8):
 global a
 return ''.join(r.choice(a) for _ in range(n))

def getOneInt(s,n=0,ord=1):                     #s=STRING,n=RETURN FIRST NCHAR,ORD=STRAIGHT OR REVERSE
 mat=re.search(r'\d+',s)
 if(mat):
  res=mat.group()
 if(n>0):
  res=res[:n]
 if(ord<0):
  res=res[::-1]
 return int(res)

def getAllInt(s):
 return re.findall(r'\d+',s)

def getDigits(s):
 return list(int(i) for i in s.split() if i.isdigit())

def dum(s,skode=1):                             #s=STRING,skode=STYLE CODE
 if(skode<100):
  skode=[s for s in range(100,999) if s%3==0][r.randint(1,256)]
 else:
  alpha=a
 div=int(len(s)/3)
 rem=int(len(s)%3)
 oso=''
 facet=[div,div,div]
 if(rem==1):
  facet[1]=div+1
 elif(rem==2):
  facet[0]=div+1
  facet[1]=div+1
 oso+=adum() +s[:facet[0]]
 oso+=adum() +s[facet[0]:-facet[2]]
 oso+=adum() +s[facet[0]+facet[1]:]
 if(skode%3==0):
  oso=str(skode)+oso+cdum()+str(len(s))+cdum()
 elif(skode%2==0):
  oso=cdum()+str(skode)+str(len(s))+cdum()+oso
 else:
  oso=cdum()+str(skode)+oso+cdum()+str(len(s))
 return oso

def redum(oso):
 point=0
 s=''
 sko=getOneInt(oso,3)
 obits=24
 if(sko%3==0):
  obits+=3
  bit=getOneInt(oso[::-1],0,-1)
  obits+=bit
  so=oso[3:obits]
 elif(sko%2==0):
  bit=int(str(getOneInt(oso))[3:])
  obits+=bit
  so=oso[::-1][:obits][::-1]
 else:
  bit=getOneInt(oso[::-1],0,-1)
  obits+=bit
  obits+=11
  so=oso[11:obits]
 div=int(bit/3)
 rem=int(bit%3)
 place=[div,div,div]
 if(rem==1):
  place[1]=div+1
 elif(rem==2):
  place[0]=div+1
  place[1]=div+1
  dbits=[]
 for ele in place:
  point+=8
  for i in range(ele):
   s+=so[point]
   point+=1
 return s

def autodum(sko=1):
 d=''.join(r.choice(a) for _ in range(r.randint(3,18)))
 return dum(d,sko)
