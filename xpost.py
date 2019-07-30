import random as R
import sys
from datetime import datetime as dtm,timedelta as tdt
from barnum import gen_data as bgdata
import json

debug=False
if len(sys.argv)<2:
    N=1
else:
    N=int(sys.argv[1])

if N<1:
    sys.exit(N)

instancelist=['swiss','US Farm','EU Farm']
deploy_mode=['Potter','IM']
auth=[{'uid':'admin','pwd':'adminpassword'},{'uid':'eaeuser','pwd':'eaeuserpassword'}
      ,{'uid':'raghu','pwd':'raghupassword'},{'uid':'yogesh','pwd':'yogeshpassword'}]

def batchPoster(n):
    reqList=[]
    for i in range(0,n):
        document={"account_name":bgdata.create_company_name(),"instancecode":R.choice(instancelist)
        ,"lms_custid":R.choice(range(69,69069)),"deploy_mode":R.choice(deploy_mode),"active":True
        ,"account_flag":R.choice([True,False]),"eae_integration":R.choice([True,False])
        ,"channel_partner":R.choice([True,False]),"onboard_type":R.choice(["custom","partner","direct"])
        ,"start_date":str(dtm.utcnow().date()-tdt(days=R.choice(range(10,1000))))}
        reqList.append(document)
    print(json.dumps(reqList))
    return None

batchPoster(N)