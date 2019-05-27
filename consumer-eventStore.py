from model import Event as E
from msgpack import unpackb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as dbeng
from confluent_kafka import Consumer
from uuid import uuid1 as uid,uuid4 as U4
from yaml import safe_load
from datetime import datetime as dtm

with open('app.yml','r') as yFile:
    cfg=safe_load(yFile)

urx='postgresql://' +str(cfg['datastore']['uid'])+ ':' +str(cfg['datastore']['pwd'])+ '@' +str(cfg['datastore']['host'])+ ':' +str(cfg['datastore']['port'])+ '/' +cfg['datastore']['db']
c=Consumer({'bootstrap.servers': cfg['kafka']['host'],'group.id': 'accounts-events','auto.offset.reset': 'earliest'})

def dataSession():
	pgx=dbeng(urx)
	SessionClass=sessionmaker(bind=pgx)
	Session=SessionClass()
	return Session

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

c.subscribe(['topic-events'])

def validateMessage(msg):
    pct=True
    if msg is None:
        pct=False
    elif msg.error():
        print('Error: {}'.format(msg.error()))
        pct=False
    return pct

while True:
    msg=c.poll(1.0)
    packet=validateMessage(msg)
    if packet:
        unp=unpackb(msg.value(),object_hook=decode_dtm,raw=False)
        unp['event_tbl_id']=U4()
        eventSession=dataSession()
        eventSession.add(E(**unp))
        print('Event Recorded...')
        eventSession.commit()
        eventSession.close()
    else:
        continue

c.close()
