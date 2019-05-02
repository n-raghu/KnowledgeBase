import sqlalchemy as say
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dtm
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid1 as uid

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
	lms_custid=COL(BIGINT,nullable=False)
	account_flag=COL(TXT)
	account_name=COL(TXT)
	deploy_mode=COL(TXT)
	eae_integration=COL(BOOL)
	channel_partner=COL(BOOL)
	onboard_type=COL(TXT)
	start_date=COL(DT)
	aid=COL(UUID(as_uuid=True),primary_key=True,default=uid())
	def __repr__(self):
		return "<A('%s')>" % (self.aid)

if __name__=='__main__':
	from resources import urx
	pge=say.create_engine(urx)
	BASE.metadata.create_all(pge)
	pge.dispose()
