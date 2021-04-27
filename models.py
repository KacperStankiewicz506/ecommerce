from sqlalchemy import Column, Integer, String
from database import Base


class Magazyn(Base):
	__tablename__ = 'magazyn'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	amount = Column(Integer)