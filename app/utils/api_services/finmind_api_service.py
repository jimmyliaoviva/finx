import requests


url = "https://api.finmindtrade.com/api/v4/data"

def get_tw_info(dataset: str):
    # url = "https://api.finmindtrade.com/api/v4/data"
    parameter = {
        "dataset": "TaiwanStockInfo",
        "token": "", # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=parameter)
    if resp.status_code != 200:
        print(f"Error: {resp.status_code}")
        raise Exception
    data = resp.json()['data']
    return data

def get_tw_stock():
    pass