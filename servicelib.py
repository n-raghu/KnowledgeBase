from msgpack import packb,unpackb
from random import randint
from flask import jsonify, abort, request, make_response, Flask
from flask_restful import Api,Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as dbeng,text as alchemyText
from datetime import datetime as dtm,timedelta as tdt
from confluent_kafka import Producer,Consumer,KafkaError

urx='postgresql://postgres:reporter@172.31.16.16:54321/statzen'
P=Producer({'bootstrap.servers': '10.0.0.10'})
Session=sessionmaker()

def delivery_report(err, msg):
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
		else:
			qpSTR=qpSTR +k+ " LIKE '" +v+ "' AND "
	if qpSTR.endswith(" AND "):
		qpSTR=qpSTR[:-5]
	return qpSTR

def encode_dtm(obj):
    if isinstance(obj, dtm):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S")}
    return obj

def getTopic():
	return 'topic-accounts'
