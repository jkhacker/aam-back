from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from datetime import timedelta

# DATABASE SETTINGS
SQLALCHEMY_DATABASE_URL = "postgresql://nikitasmirnov:5931@localhost/aam"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# JWT TOKEN SETTINGS
SECRET_KEY = "d945b73c123e1c8ff216bd5c0d19e5fc185dac512030ee545dc065e390232bf6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

# HASHING SETTINGS
PWDContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
