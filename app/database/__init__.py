from sqlalchemy.ext.declarative import declarative_base
from .database import session_scope

Base = declarative_base()



from .taiwan_stock_info import TaiwanStockInfo
from .taiwan_stock_price import TaiwanStockPrice