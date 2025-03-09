import requests


def get_data(dataset: str):
    url = "https://api.finmindtrade.com/api/v4/data"
    parameter = {
        "dataset": "TaiwanStockInfo",
        "token": "", # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=parameter)
    if resp.status_code != 200:
        print(f"Error: {resp.status_code}")
        return
    data = resp.json()['data']
    return data