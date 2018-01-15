from cryptography.fernet import Fernet as frt
from addendum import r,adum,apath
import os

binPath=apath('bin')
keys=set()

while 1:
 keybin=binPath+adum(4)
 if(os.path.isfile(keybin)==False):
  break

kline=r.randint(500001,1402117)
for i in range(kline):
 key=frt.generate_key()
 keys.add(key.decode())

# FILE OPS
with open(keybin, 'w') as file_handler:
    for item in keys:
        file_handler.write('{}\n'.format(item))

print('New BIN created with ' +str(kline)+ ' keys')
