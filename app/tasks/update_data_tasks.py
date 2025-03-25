# Keep your tasks in tasks.py small and readable
# Don't place your business logic in it, just import them here

from app.tasks.celery import app
from app.utils import finmind_api_service
from app.database import TaiwanStockInfo, session_scope


@app.task(autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 5})
def update_tw_price_t() -> None:
    try:
        data = finmind_api_service.get_info("TaiwanStockPrice")
        with session_scope() as session:
            TaiwanStockInfo.upsert_tw_stock_price(session, data)
        print("update_tw_price done")
    except Exception as e:
        print(f"fail to update, exception: {e}")

@app.task(autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 5})
def update_tw_info_t() -> None:
    try:
        data = finmind_api_service.get_info("TaiwanStockInfo")
        unique_data = {item['stock_id']: item for item in data}.values()
        with session_scope() as session:
            TaiwanStockInfo.upsert_tw_stock_info(session, unique_data)
        print("update_tw_info done")
    except Exception as e:
        print(f"fail to update, exception: {e}")
