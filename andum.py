import string as stg, random as r

c=stg.ascii_letters
a=c+stg.digits

def dum(s,skode=1,n=8,anm=1):
 if(skode<100):
  skode=[s for s in range(100,999) if s%3==0][r.randint(1,256)]
 if(anm!=1):
  alpha=c
 else:
  alpha=a
 div=int(len(s)/3)
 rem=int(len(s)%3)
 oso=''
 facet=[div,div,div]
 if(rem==1):
  facet[1]=div+1
 if(rem==2):
  facet[0]=div+1
  facet[1]=div+1
 oso+=''.join(r.choice(alpha) for _ in range(n)) + s[:facet[0]]
 oso+=''.join(r.choice(alpha) for _ in range(n)) + s[facet[0]:-facet[2]]
 oso+=''.join(r.choice(alpha) for _ in range(n)) + s[facet[0]+facet[1]:]
 oso=str(skode)+oso+str(len(s))
 return oso

def redum(s,n=8,p=0):
 if(p==-1):
  oso=s[n:]
 if(p==0):
  fno=int(n/2)
  lno=int(n-fno)
  oso=s[lno:-fno]
 if(p==1):
  oso=s[:n]
 return oso

def autodum(sko=1):
 d=''.join(r.choice(a) for _ in range(r.randint(5,25)))
 print(d)
 x= dum(d,1)
 print(x)
 return len(x)
