import bson
from addendum import r, apath, uid, stg

print('Name the Code File : ')
fnm=input()
loc=apath('lib')
fnm=loc+fnm
pid=bson.objectid.ObjectId()

dfile=open(fnm, 'w')
dfile.write(str(pid))
print('File Created...')

diSet=set()
dicto=[list(stg.ascii_uppercase), list(stg.ascii_lowercase),list(stg.digits),list(stg.punctuation)]
dKeys=[]
dod = [0,1,2,3]
r.shuffle(dod)

for i in range(r.randint(140217,360066)):
  tdict=[]
  for ele in dod:
   mys = dicto[ele]
   r.shuffle(mys)
   tdict+=mys
  r.shuffle(tdict)
  fst=''.join(map(str,tdict))
  diSet.add(fst)
print(str(len(diSet)) +' Dictionaries created. Generating Keys...')
diSet=list(diSet)
for i in range(len(diSet)):
    dKeys.append(uid.uuid4().hex)

#FILE
for ele in range(len(diSet)):
 dfile.write('\n')
 dfile.write(diSet[ele] +'\t'+ dKeys[ele])
dfile.close()

print('Dictionary File ' +fnm+ ' created with ' +str(len(diSet))+ ' dictionaries.')
diSet=[]
dKeys=[]
