import requests
import pytest
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    param = base_data.read_data()["mobile_phone_belong"]  # 直接获取字典
    print("测试手机号 post 请求")

    r = requests.post(url + "/shouji/query",
        params={
          "shouji": param['shouji'],
          "appkey": param['appkey']
        }
    )
    assert r.status_code == 200
    # 打印或处理响应
    print(r.status_code)