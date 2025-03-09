from . import Base
from sqlalchemy import Column, String, Date, DateTime
from datetime import datetime

class TaiwanStockInfo(Base):
    __tablename__ = 'TaiwanStockInfo'
    industry_category = Column(String(30), primary_key=True, nullable=False, comment='Industry Category')
    stock_id = Column(String(50), primary_key=True, nullable=False, comment='Stock ID')
    stock_name = Column(String(30), nullable=True, comment='Stock Name')
    type = Column(String(10), nullable=False, comment='上市twse/上櫃tpex')
    date = Column(Date, nullable=True, comment='Date')
    create_time = Column(DateTime, nullable=False, default=datetime.utcnow, comment='Create Time')

    @classmethod
    def get_all_tw_stock_info(cls,session):
        return session.query(cls).all()

    @classmethod
    def upsert_tw_stock_info(cls, session, data):
        for item in data:
            if item.get('date') == 'None':
                item['date'] = None
            session.merge(cls(**item))