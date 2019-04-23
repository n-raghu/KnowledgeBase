import sqlalchemy as say
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dtm

BASE=declarative_base()

COL=say.Column
INT=say.Integer
BOOL=say.Boolean
BIGINT=say.BIGINT
FLOAT=say.Float
TABLE=say.Table
STR=say.String
TXT=say.Text
TIME=say.TIME
TIMES=say.TIMESTAMP
DT=say.Date
NUM=say.NUMERIC

class Account(BASE):
	__tablename__='accounts'
	instancecode=COL(TXT)
	lms_custid=COL(BIGINT)
	aid=COL(NUM(64,0),primary_key=True)
	account_flag=COL(TXT)
	account_name=COL(TXT)
	deploy_mode=COL(TXT)
	eae_integration=COL(BOOL)
	channel_partner=COL(BOOL)
	onboard_type=COL(TXT)
	start_date=COL(DT)
	last_updated_time=COL(TIMES,default=dtm.utcnow(),onupdate=dtm.utcnow())
	def __repr__(self):
		return "<A('%s')>" % (self.aid)

if __name__=='__main__':
	from resources import urx
	pge=say.create_engine(urx)
	BASE.metadata.create_all(pge)
	pge.dispose()
