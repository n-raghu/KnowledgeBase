import math
from sqlalchemy.orm import sessionmaker
from datetime import datetime as dtm
from sqlalchemy import create_engine as dbeng,text as alchemyText

class Page(object):
    def __init__(self,items,page,page_size,total):
        self.items=items
        self.previous_page=None
        self.next_page=None
        self.has_previous=page>1
        if self.has_previous:
            self.previous_page = page - 1
        previous_items=(page-1)*page_size
        self.has_next=previous_items+len(items)<total
        if self.has_next:
            self.next_page=page+1
        self.total=total
        self.pages=int(math.ceil(total/float(page_size)))

def dataSession(urx):
	pgx=dbeng(urx)
	SessionClass=sessionmaker(bind=pgx)
	Session=SessionClass()
	return Session

def delivery_report(err,msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def queryParser(qList):
	nuList=[]
	qpSTR=" "
	for k,v in qList.items():
		if k.endswith('__between__'):
			kSTR=k[:-11]
			values2=v.split(',')
			qpSTR=qpSTR +kSTR+ " BETWEEN '" +values2[0]+ "' AND '" +values2[1]+ "' AND "
		elif v=='true' or v=='false':
			qpSTR=qpSTR +k+ "='" +v+ "' AND "
		else:
			qpSTR=qpSTR +k+ " LIKE '" +v+ "' AND "
	if qpSTR.endswith(" AND "):
		qpSTR=qpSTR[:-5]
	return qpSTR

def encode_dtm(obj):
    if isinstance(obj, dtm):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S")}
    return obj

def paginate(query,page,page_size=100):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')
    items=query.limit(page_size).offset((page - 1)*page_size).all()
    total=query.order_by(None).count()
    return Page(items,page,page_size,total)
