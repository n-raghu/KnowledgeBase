import requests as req
import random as R
import sys
from datetime import datetime as dtm,timedelta as tdt
from uuid import uuid1 as uid

point='http://172.31.16.16:39099/accounts'
headers={'content-type':'application/json'}

if len(sys.argv)<2:
    batch=1
else:
    batch=float(sys.argv[1])

instancelist=['swiss','US Farm','EU Farm']
companylist=['NorthernFirm','WestEnterprise','NuSyndicate','NewUnion','CastBox']
deploy_mode=['Potter','IM']

def batchPoster(n=10):
    reqList=[]
    for i in range(0,n):
        company=R.choice(companylist) +'-'+ chr(R.choice(range(65,90)))
        document={"account_name":company,"instancecode":R.choice(instancelist)
        ,"lms_custid":R.choice(range(69,69069)),"deploy_mode":R.choice(deploy_mode)
        ,"account_flag":R.choice([True,False]),"eae_integration":R.choice([True,False])
        ,"channel_partner":R.choice([True,False]),"onboard_type":R.choice(["custom","partner","direct"])
        ,"start_date":str(dtm.utcnow().date()-tdt(days=R.choice(range(10,1000))))}
        reqList.append(document)
    return req.post(url=point,json=reqList,verify=False),reqList

idi=0
qpo=[]

while True:
    qpo.append(batchPoster())
    idi+=1
    d=int(10*(batch-idi))
    if d>1 and d<10:
        qpo.append(batchPoster(d))
        break
    elif d<1:
        break
    else:
        continue

print(qpo)
