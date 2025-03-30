from ..datasource_provider import DatasourceProvider
from app.utils.api_services import finmind_api_service

class FinlabService(DatasourceProvider):
    """
    FinlabService is a class that provides methods to interact with the Finlab API.
    It includes methods to fetch stock data, financial statements, and other related information.
    """

    def __init__(self):
        pass
    
    def _get_tw_stock_info(self):
        """
        Fetch all stock data for Taiwan.

        Returns:
            dict: The stock data.
        """
        data = finmind_api_service.get_tw_info("TaiwanStockInfo")
        unique_data = {item['stock_id']: item for item in data}.values()
        return unique_data
    
    def get_all_stocks_info(self, country: str):
        """
        Fetch stock data for a given country

        Args:
            country (str): The country alias to fetch data for.

        Returns:
            dict: The stock data.
        """
        if country == "TW":
            return self._get_tw_stock_info()

