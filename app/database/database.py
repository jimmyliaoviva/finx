from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from app.utils import config

host = config.get_db_host()
user = config.get_db_user()
password = config.get_db_password()
database = config.get_db_name()


engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session_scope():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()