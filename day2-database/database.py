from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Format: mysql+pymysql://username:password@host/database_name
DATABASE_URL = "mysql+pymysql://root:hello123@localhost/fastapi_learning"

# Create engine (connection to DB)
engine = create_engine(DATABASE_URL)

# Each request gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# Dependency — gives DB session to each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()