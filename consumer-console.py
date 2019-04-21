from confluent_kafka import Consumer, KafkaError
from msgpack import unpackb
from datetime import datetime as dtm
import sys

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

c=Consumer({
    'bootstrap.servers': '10.0.0.10',
    'group.id': 'accounts-console',
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
    print('Received message: {}'.format(msg.value()) +', Message Size: '+ str(sys.getsizeof(msg.value())))
    unp=unpackb(msg.value(),object_hook=decode_dtm,raw=False)
    print(unp)
    print('Size after Unpacking: ' +str(sys.getsizeof(unp)))
    print(' ')

c.close()
