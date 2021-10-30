import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:aezakmi322@localhost/RestApi_blog"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
