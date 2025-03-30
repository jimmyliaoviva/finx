# Keep your tasks in tasks.py small and readable
# Don't place your business logic in it, just import them here

from app.tasks.celery import app
from app.utils.api_services import finmind_api_service
from app.database import TaiwanStockInfo, session_scope
from app.utils.datasource_handler.datasource_provider import DatasourceProviderFactory, DatasourceType

@app.task(autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 5})
def update_tw_price_t() -> None:
    pass

@app.task(autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 5})
def update_tw_info_t() -> None:
    try:
        datasourceService = DatasourceProviderFactory.get_datasource_provider(DatasourceType.FINLAB)
        data = datasourceService.get_all_stocks_info("TW")
        with session_scope() as session:
            TaiwanStockInfo.upsert_tw_stock_info(session, data)
        print("update_tw_info done")
    except Exception as e:
        print(f"fail to update, exception: {e}")
