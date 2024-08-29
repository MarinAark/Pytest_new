import requests


def test_mobile(self):
    r = requests.get(url="http://api.binstd.com/shouji/query", params={
        "shouji": "13456755448",
        "appkey": "0c818521d38759e1"})
    result = r.json()

