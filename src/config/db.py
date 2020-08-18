import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DB_URL, pool_size=20, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
