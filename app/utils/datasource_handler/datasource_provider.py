import abc

class DatasourceType:
  """
  Register different type of datasource.
  """
  FINLAB = "finlab"

class DatasourceProviderFactory:
  @staticmethod
  def get_datasource_provider(datasource_type: str):
    """
    Returns a datasource provider based on the datasource type.
    """
    if datasource_type == DatasourceType.FINLAB:
      from .finlab.finlab_service import FinlabService
      return FinlabService()
    else:
      raise ValueError(f"Unsupported datasource type: {datasource_type}")
    

class DatasourceProvider(metaclass=abc.ABCMeta):
  """
  DatasourceProvider is a base class for all datasource providers.
  It provides a common interface for fetching data from different sources.
  """
  def __init__(self):
    pass

  @abc.abstractmethod
  def get_all_stocks_info(self, country: str):
    """
    Fetch stock data for a given stock ID.

    Args:
        stock_id (str): The stock ID to fetch data for.

    Returns:
        dict: The stock data.
    """
    pass