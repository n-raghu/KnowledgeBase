from msgpack import unpackb
from confluent_kafka import Consumer

c=Consumer({'bootstrap.servers': '10.0.0.10','group.id': 'accounts-data','auto.offset.reset': 'earliest'})

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
		print(unp)
    else:
        continue

c.close()
