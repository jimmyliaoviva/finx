from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(
    "mysql+pymysql://root:jimmy@localhost/finx?charset=utf8mb4"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session_scope():
    session = SessionLocal()
    if not session.in_transaction():
        with session.begin():
            try:
                yield session
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
    else:
        yield session

