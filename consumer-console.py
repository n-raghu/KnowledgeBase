from msgpack import unpackb
from confluent_kafka import Consumer
from yaml import safe_load

with open('app.yml','r') as yFile:
    cfg=safe_load(yFile)

c=Consumer({'bootstrap.servers':str(cfg['kafka']['host']),'group.id':'accounts-console','auto.offset.reset':'earliest'})

def decode_dtm(obj):
    if '__datetime__' in obj:
        obj=dtm.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S")
    return obj

topics=['topic-accounts-patch','topic-accounts-purge','topic-accounts-add','topic-events']
c.subscribe(topics)

while True:
    msg=c.poll(1.0)
    print(msg.topic)

c.close()
