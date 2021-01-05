import sys

from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dburi = 'postgresql://pgusr:pgusr@gqldb/gdb'
dbeng = create_engine(dburi)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=dbeng,
    )
)

Base = declarative_base()
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    isactive = Column(BOOLEAN)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(dbeng)
    dbeng.dispose()
