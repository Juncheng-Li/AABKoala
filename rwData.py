from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataPoint(Base):
    __tablename__ = 'dataPoint'

    x = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:AAkoala123456@koala:3306/test')
DBSession = sessionmaker(bind=engine)


