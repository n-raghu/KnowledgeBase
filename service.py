import sys
if len(sys.argv)<2:
	pwd='nuPassword'
else:
	pwd=sys.argv[1]

from resources import Account as A,dataSession
from servicelib import *

app=Flask(__name__)
app.config['JWT_SECRET_KEY']='eaeadmin'
jwt=JWTManager(app)
api=Api(app)

class getPostAcc(Resource):
	def get(self):
		jlist=[]
		qpm=request.args
		eventSession=dataSession()
		if len(qpm)==1:
			for k,v in qpm.items():
				col=k
				val=v
			if val.startswith('%') and val.endswith('%'):
				xClass=eventSession.query(A).filter(getattr(A,col).like('%%%s%%' % val))
			elif k.endswith('__between__'):
				xClass=eventSession.query(A).filter(alchemyText(queryParser(qpm))).all()
			else:
				xClass=eventSession.query(A).filter(getattr(A,col)==val)
		elif len(qpm)>1:
			xClass=eventSession.query(A).filter(alchemyText(queryParser(qpm))).all()
		else:
			xClass=eventSession.query(A).all()
		eventSession.close()
		for x in xClass:
			x.__dict__.pop('_sa_instance_state',None)
			jlist.append(x.__dict__)
		return jsonify(jlist)

	def post(self):
		if not request.get_json():
			abort(400)
		obo=request.get_json()
		print(obo)
		P.poll(0)
        P.produce(getTopic(),packb(obo,default=encode_dtm,use_bin_type=True),callback=delivery_report)
		return None

class AccountID(Resource):
	@jwt_required
	def get(self,accid):
		user=get_jwt_identity()
		if user!=pwd:
			return jsonify({'response':'Incorrect/Tampered Token'})
		print(user)
		eventSession=dataSession()
		xClass=eventSession.query(A).filter(A.aid==accid)
		eventSession.close()
		jlist=[]
		for x in xClass:
			x.__dict__.pop('_sa_instance_state',None)
			jlist.append(x.__dict__)
		return jsonify(jlist)
	def delete(self,accid):
		eventSession=dataSession()
		dataObj=eventSession.query(A).filter(A.aid==accid).delete()
		eventSession.commit()
		eventSession.close()
		return jsonify({'response': str(accid)+ ' deleted.'})
	def put(self,accid):
		obo=request.get_json()
		eventSession=dataSession()
		dataObj=eventSession.query(A).filter(A.aid==accid)
		eventSession.close()
		for x in dataObj:
			x.__dict__.pop('_sa_instance_state',None)
			datax=x.__dict__
		datax.update(obo)
		eventSession=dataSession()
		dataObj=eventSession.query(A).filter(A.aid==accid).delete()
		eventSession.commit()
		eventSession.close()
		eventSession=dataSession()
		eventSession.add(A(**datax))
		eventSession.commit()
		eventSession.close()
		return None

class getNewToken(Resource):
	def post(self):
		if not request.get_json():
			abort(400)
		obo=request.get_json()
		username=request.json.get('username',None)
		access_token=create_access_token(identity=username,expires_delta=tdt(seconds=36))
		return jsonify(access_token)

api.add_resource(getPostAcc,'/accounts')
api.add_resource(AccountID,'/accounts/<int:accid>')
api.add_resource(getNewToken,'/accounts/login')

app.run(debug=True,host='0.0.0.0',port=39099)
