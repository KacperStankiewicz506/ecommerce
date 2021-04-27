from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:calculator@localhost:5000/commerce"

engine = create_engine(
     SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(engine)

Base = declarative_base()