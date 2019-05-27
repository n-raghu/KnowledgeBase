import sqlalchemy as say
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dtm
from sqlalchemy.dialects.postgresql import UUID

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
	active=COL(BOOL)
	account_name=COL(TXT)
	aid=COL(UUID(as_uuid=True),primary_key=True)
	instancecode=COL(TXT)
	lms_custid=COL(BIGINT,nullable=False)
	account_flag=COL(TXT)
	deploy_mode=COL(TXT)
	eae_integration=COL(BOOL)
	channel_partner=COL(BOOL)
	onboard_type=COL(TXT)
	start_date=COL(DT)
	def __repr__(self):
		return "<A('%s')>" % (self.aid)

class Event(BASE):
	__tablename__='events'
	eventid=COL(TXT)
	etime=COL(TIMES)
	event=COL(TXT)
	action=COL(TXT)
	event_owner=COL(TXT,primary_key=True)
	event_tbl_id=COL(UUID(as_uuid=True),primary_key=True)

class User(BASE):
	__tablename__='users'
	uid=COL(TXT,primary_key=True)
	pwd=COL(TXT)
	user_name=COL(TXT)
	roleid=COL(INT)

class Role(BASE):
	__tablename__='userroles'
	rid=COL(INT,primary_key=True)
	rolename=COL(TXT)
	tokentime=COL(INT)

if __name__=='__main__':
	from resources import urx
	pge=say.create_engine(urx)
	BASE.metadata.create_all(pge)
	pge.dispose()
