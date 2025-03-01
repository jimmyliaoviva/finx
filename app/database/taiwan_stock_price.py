from . import Base
from sqlalchemy import Column, BigInteger, Date, Float, String

class TaiwanStockPrice(Base):
    __tablename__ = 'TaiwanStockPrice'
    date = Column(Date, nullable=False, primary_key=True)
    Trading_Volume = Column(BigInteger, nullable=True)
    Trading_money = Column(BigInteger, nullable=True)
    open = Column(Float, nullable=True)
    max = Column(Float, nullable=True)
    min = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    spread = Column(Float, nullable=True)
    Trading_turnover = Column(BigInteger, nullable=True)
    stock_id = Column(String(100), nullable=False, primary_key=True)
