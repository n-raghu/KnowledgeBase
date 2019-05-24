from model import Account as A
from msgpack import packb,unpackb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as dbeng
from confluent_kafka import Producer,Consumer,KafkaError
from uuid import uuid1 as uid
from yaml import safe_load
from datetime import datetime as dtm

with open('app.yml','r') as yFile:
    cfg=safe_load(yFile)

urx='postgresql://' +str(cfg['datastore']['uid'])+ ':' +str(cfg['datastore']['pwd'])+ '@' +str(cfg['datastore']['host'])+ ':' +str(cfg['datastore']['port'])+ '/' +cfg['datastore']['db']
C=Consumer({'bootstrap.servers': cfg['kafka']['host'],'group.id': 'accounts-data','auto.offset.reset': 'earliest'})
P=Producer({'bootstrap.servers': cfg['kafka']['host']})

def dataSession():
	pgx=dbeng(urx)
	SessionClass=sessionmaker(bind=pgx)
	Session=SessionClass()
	return Session

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

def encode_dtm(obj):
    if isinstance(obj, dtm):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S")}
    return obj

def delivery_report(err,msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

C.subscribe(['topic-accounts-patch','topic-accounts-purge','topic-accounts-add'])

def validateMessage(msgTup):
    pct=True
    msg,_,_=msgTup
    if msg is None:
        pct=False
    elif msg.error():
        print('Error: {}'.format(msg.error()))
        pct=False
    return pct

while True:
    msgTup=C.poll(1.0)
    packet=validateMessage(msgTup)
    if packet:
        msg,ebsonid,eventClass=msgTup
        unp=unpackb(msg.value(),object_hook=decode_dtm,raw=False)
        eventSession=dataSession()
        if msg.topic()=='topic-accounts-patch':
            eventSession.query(A).filter(A.aid==unp['aid']).update(unp)
        elif msg.topic()=='topic-accounts-purge':
            eventSession.query(A).filter(A.aid==unp['aid']).update(unp)
        elif msg.topic()=='topic-accounts-add':
            if isinstance(unp,list):
                print('Streaming list of ' +str(len(unp))+ ' accounts...')
                unpAccounts=[]
                for u in unp:
                    u['aid']=uid()
                    unpAccounts.append(u)
                unpList=[A(**u) for u in unpAccounts]
                eventSession.add_all(unpList)
            else:
                unp['aid']=uid()
                eventSession.add(A(**unp))
                print('One account...')
        eventSession.commit()
        eventDoc={'event':eventClass,'action':'__close_event__','etime':dtm.utcnow(),'event_owner':'__consumer__','eventid':ebsonid}
        P.poll(0)
        P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
        eventSession.close()
    else:
        continue

C.close()
