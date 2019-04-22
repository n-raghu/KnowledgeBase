from model import Account as A
from msgpack import unpackb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as dbeng
from confluent_kafka import Consumer

urx='postgresql://postgres:reporter@172.31.16.16:54321/statzen'
c=Consumer({'bootstrap.servers': '10.0.0.10','group.id': 'accounts-data','auto.offset.reset': 'earliest'})

def dataSession():
	pgx=dbeng(urx)
	SessionClass=sessionmaker(bind=pgx)
	Session=SessionClass()
	return Session

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

c.subscribe(['topic-accounts-patch','topic-accounts-purge'])

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
        eventSession=dataSession()
        if isinstance(unp,list):
            print('Streaming list of ' +str(len(unp))+ ' accounts...')
            unpList=[A(**u) for u in unp]
            eventSession.add_all(unpList)
        else:
            eventSession.add(A(**unp))
            print('One account...')
        eventSession.commit()
        eventSession.close()
    else:
        continue

c.close()
