import requests as req
import random as R
import sys
from datetime import datetime as dtm,timedelta as tdt
from uuid import uuid1 as uid
from yaml import safe_load
from requests_jwt import JWTAuth
from barnum import gen_data as bgdata

with open('app.yml') as ymlFile:
    cfg=safe_load(ymlFile)

point='http://172.16.1.164:39099/accounts'
access='http://172.16.1.164:39099/login'
N=10000
headers={'content-type':'application/json'}

debug=False
if len(sys.argv)<2:
    batch=1
else:
    batch=float(sys.argv[1])
    if batch==-1:
        debug=True
        batch=1

instancelist=['swiss','US Farm','EU Farm']
deploy_mode=['Potter','IM']
auth=[{'uid':'admin','pwd':'adminpassword'},{'uid':'eaeuser','pwd':'eaeuserpassword'}
      ,{'uid':'raghu','pwd':'raghupassword'},{'uid':'yogesh','pwd':'yogeshpassword'}]

def getToken():
    thisAuth=R.choice(auth)
    token=req.post(url=access,json=thisAuth,verify=False)
    return token

def batchPoster(n=N):
    reqList=[]
    for i in range(0,n):
        document={"account_name":bgdata.create_company_name(),"instancecode":R.choice(instancelist)
        ,"lms_custid":R.choice(range(69,69069)),"deploy_mode":R.choice(deploy_mode),"active":True
        ,"account_flag":R.choice([True,False]),"eae_integration":R.choice([True,False])
        ,"channel_partner":R.choice([True,False]),"onboard_type":R.choice(["custom","partner","direct"])
        ,"start_date":str(dtm.utcnow().date()-tdt(days=R.choice(range(10,1000))))}
        reqList.append(document)
    t=getToken()
    dataHeadR={'Content-Type':'application/json','Authorization':'Bearer {}'.format(t.json())}
    print(dataHeadR)
    print(len(reqList))
    return req.post(url=point,json=reqList,headers=dataHeadR)

idi=0
qpo=[]

if not debug:
    while True:
        qpo.append(batchPoster())
        idi+=1
        d=int(N*(batch-idi))
        if d>1 and d<N:
            qpo.append(batchPoster(d))
            break
        elif d<1:
            break
        else:
            continue

print(qpo)
