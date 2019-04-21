from confluent_kafka import Producer
from msgpack import packb,unpackb
from datetime import datetime as dtm
from time import sleep as ziz

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

def encode_dtm(obj):
    if isinstance(obj, dtm):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S")}
    return obj

p=Producer({'bootstrap.servers': '10.0.0.10'})
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

some_data_source=[{'a':5,'d':dtm.utcnow()},{'d':dtm.utcnow(),'x':'nuSTR'}]
i=0

while True:
    for dat in some_data_source:
        p.poll(0)
        data=dat.copy()
        data['itr']=i
        p.produce('topic-accounts', packb(data,default=encode_dtm,use_bin_type=True),callback=delivery_report)
    i+=1
    ziz(8)

p.flush()
