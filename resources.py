from msgpack import packb
from random import randint
from flask import jsonify, abort, request, make_response, Flask
from flask_restful import Api,Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity,jwt_optional)
from datetime import datetime as dtm,timedelta as tdt
from confluent_kafka import Producer,Consumer,KafkaError
from model import Account as A,User as U,UserRole as UR
from yaml import safe_load
from alchemy import paginate,dataSession
from bson.objectid import ObjectId as bsonid

with open('app.yml') as ymlFile:
    cfg=safe_load(ymlFile)

urx='postgresql://' +cfg['datastore']['uid']+ ':' +cfg['datastore']['pwd']+ '@' +cfg['datastore']['host']+ ':' +str(cfg['datastore']['port'])+ '/' +cfg['datastore']['db']
P=Producer({'bootstrap.servers': cfg['kafka']['host']})

def getTopic(eve='get'):
    if eve=='add':
        v_eve='topic-accounts-add'
    elif eve=='patch':
        v_eve='topic-accounts-patch'
    elif eve=='purge':
        v_eve='topic-accounts-purge'
    elif eve=='get':
        v_eve='topic-accounts-get'
    else:
        v_eve=False
    return v_eve

class getPostAcc(Resource):
	@jwt_optional
	def get(self):
		jlist=[]
		qpx=request.args
		qpm=qpx.to_dict(flat=True)
		rpage=request.args.get('__page__',1,type=int)
		eventSession=dataSession(urx)
		if '__page__' in qpm:
			del qpm['__page__']
		if len(qpm)==1:
			for k,v in qpm.items():
				col=k
				val=v
			if val.startswith('%') and val.endswith('%'):
				xClass=paginate(eventSession.query(A).filter(A.active==True,getattr(A,col).like('%%%s%%' % val)),rpage)
			elif k.endswith('__between__'):
				xClass=paginate(eventSession.query(A).filter(A.active==True,alchemyText(queryParser(qpm))),rpage)
			else:
				xClass=paginate(eventSession.query(A).filter(A.active==True,getattr(A,col)==val),rpage)
		elif len(qpm)>1:
			xClass=paginate(eventSession.query(A).filter(A.active==True,alchemyText(queryParser(qpm))),rpage)
		else:
			xClass=paginate(eventSession.query(A).filter(A.active==True),rpage)
		eventSession.close()
		for x in xClass.items:
			x.__dict__.pop('_sa_instance_state',None)
			jlist.append(x.__dict__)
		eowner=get_jwt_identity()
		if not eowner:
			eowner='anonymous call...'
		eventDoc={'event':getTopic(),'action':'get','etime':dtm.utcnow(),'event_owner':eowner,'eventid':str(bsonid())}
		P.poll(0)
		P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		responser=make_response(jsonify(jlist),200)
		responser.headers.extend({'page':rpage,'total':xClass.pages})
		return responser

	@jwt_required
	def post(self):
		if not request.get_json():
			abort(400)
		obo=request.get_json()
		thisTopic=getTopic('add')
		if isinstance(obo,list):
			etype='bulk'
		else:
			etype='one'
		ebsonid=str(bsonid())
		eventDoc={'event':thisTopic,'action':etype,'etime':dtm.utcnow(),'event_owner':get_jwt_identity(),'eventid':ebsonid}
		P.poll(0)
		P.produce(thisTopic,packb((obo,ebsonid,thisTopic),default=encode_dtm,use_bin_type=True),callback=delivery_report)
		P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return None

class AccountID(Resource):
	@jwt_required
	def get(self,accid):
		eventSession=dataSession(urx)
		xClass=eventSession.query(A).filter(A.aid==accid)
		eventSession.close()
		jlist=[]
		for x in xClass:
			x.__dict__.pop('_sa_instance_state',None)
			jlist.append(x.__dict__)
		eventDoc={'event':getTopic(),'action':'get-id','etime':dtm.utcnow(),'event_owner':get_jwt_identity(),'eventid':str(bsonid())}
		P.poll(0)
		P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return jsonify(jlist)

	@jwt_required
	def delete(self,accid):
		obo={'aid':accid,'active':False}
		thisTopic=getTopic('purge')
		ebsonid=str(bsonid())
		eventDoc={'event':thisTopic,'action':'purge','etime':dtm.utcnow(),'event_owner':get_jwt_identity(),'eventid':ebsonid}
		P.poll(0)
		P.produce(thisTopic,packb((obo,ebsonid,thisTopic),default=encode_dtm,use_bin_type=True),callback=delivery_report)
		P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return None

	@jwt_required
	def put(self,accid):
		obo=request.get_json()
		obo['aid']=accid
		thisTopic=getTopic('patch')
		ebsonid=str(bsonid())
		eventDoc={'event':thisTopic,'action':'patch','etime':dtm.utcnow(),'event_owner':get_jwt_identity(),'eventid':ebsonid}
		P.poll(0)
		P.produce(thisTopic,packb((obo,ebsonid,thisTopic),default=encode_dtm,use_bin_type=True),callback=delivery_report)
		P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return None

class getNewToken(Resource):
	def post(self):
		if not request.get_json():
			abort(400)
		obo=request.get_json()
		access_token='Unauthorized User...'
		uname=request.json.get('uid',None)
		paswd=request.json.get('pwd',None)
		eventSession=dataSession(urx)
		userdoc=eventSession.query(U).filter(U.uid==uname).first()
		eventSession.close()
		if paswd==userdoc.__dict__['pwd']:
			eventSession=dataSession(urx)
			roledoc=eventSession.query(UR).filter(UR.rid==userdoc.__dict__['roleid']).first()
			eventSession.close()
			tokenTime=roledoc.__dict__['tokentime']
			if tokenTime==-1:
				access_token=create_access_token(identity=uname,expires_delta=tdt(seconds=3116969069))
			else:
				access_token=create_access_token(identity=uname,expires_delta=tdt(seconds=tokenTime))
			eventDoc={'event':'access-tokens','action':'gen-access-token','etime':dtm.utcnow(),'event_owner':uname,'eventid':str(bsonid())}
			P.poll(0)
			P.produce('topic-events',packb(eventDoc,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return jsonify(access_token)
