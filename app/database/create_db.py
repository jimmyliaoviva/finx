from . import Base
from sqlalchemy import create_engine
from app.utils import config

host = config.get_db_host()
user = config.get_db_user()
password = config.get_db_password()
database = config.get_db_name()

print(f"Connecting to database {database} at {host} with user {user}")
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4"
)

#Create all tables
Base.metadata.create_all(engine)

print("Database created")