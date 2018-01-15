from cryptography.fernet import InvalidToken, Fernet as frt

def cypher(kmap,s,key):
 f=frt(key)
 token=f.encrypt(s.encode())
 token=kmap[1:3][::-1]+token.decode()+kmap[3:4]+kmap[:1]
 return token

def deCypher(s,keys):
 myStr=''
 s=s[2:-2]
 token=s.encode()
 for key in keys:
  f=frt(key)
  try:
   f.decrypt(token)
  except InvalidToken:
   continue
  myStr=f.decrypt(token).decode()
  break
 keys=[]
 return myStr
