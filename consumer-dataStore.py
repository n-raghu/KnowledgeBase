from servicelib import *

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

c=Consumer({
    'bootstrap.servers': '10.0.0.10',
    'group.id': 'accounts-data',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['topic-accounts'])

while True:
    msg=c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    unp=unpackb(msg.value(),object_hook=decode_dtm,raw=False)
    eventSession=dataSession()
    eventSession.add(A(**unp))
    eventSession.commit()
    eventSession.close()

c.close()
