from . import Base
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://root:jimmy@localhost/finx?charset=utf8mb4"
)

#Create all tables
Base.metadata.create_all(engine)

print("Database created")