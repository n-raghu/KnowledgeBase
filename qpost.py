import requests as req
import random as R
import sys
from uuid import uuid1 as uid
from datetime import datetime as dtm,timedelta as tdt

point='172.31.16.16/accounts'

if len(sys.args)<2:
    batch=1
else:
    batch=float(sys.args[1])

instancelist=['swiss','US Farm','EU Farm']
companylist=['NorthernFirm','WestEnterprise','NuSyndicate','NewUnion','CastBox']
deploy_mode=['Potter','IM']

def batchPoster(n=1000):
    reqList=[]
    for i in range(0,n):
        company=R.choice(companylist) +'-'+ chr(R.choice(range(65,90)))
        aid=uid().int
        document={"aid":aid,"account_name":company,"instancecode":R.choice(instancelist),"lms_custid":aid
        ,"deploy_mode":R.choice(deploy_mode),"account_flag":R.choice([True,False])
        ,"eae_integration":R.choice([True,False]),"channel_partner":R.choice([True,False])
        ,"onboard_type":R.choice(["custom","partner","direct"]),"start_date":dtm.utcnow()-tdt(days=R.choice(range(10,1000)))}
        reqList.append(document)
    return req.posts(url=point,data=reqList)

idi=0
qpo=[]

while True:
    qpo.append(batchPoster())
    idi+=1
    d=int(1000*(batch-idi))
    if d>1 and d<1000:
        qpo.append(batchPoster(d))
        break
    elif d<1:
        break
    else:
        continue

print(qpo)
