from model import Account as A
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine as dbeng,text as alchemyText
from datetime import datetime as dtm,timedelta as tdt
from yaml import safe_load

with open('app.yml') as ymlFile:
    cfg=safe_load(ymlFile)

urx='postgresql://' +cfg['datastore']['uid']+ ':' +cfg['datastore']['pwd']+ '@' +cfg['datastore']['host']+ ':' +str(cfg['datastore']['port'])+ '/' +cfg['datastore']['db']

def dataSession():
	pgx=dbeng(urx)
	SessionClass=sessionmaker(bind=pgx)
	Session=SessionClass()
	return Session

def getUser(accid):
    eventSession=dataSession()
    xClass=eventSession.query(A).filter(A.aid==accid)
    eventSession.close()
    return xClass




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
