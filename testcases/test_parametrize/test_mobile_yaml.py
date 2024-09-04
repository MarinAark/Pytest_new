import requests
import pytest
from utils.read_data import get_data
from utils.read_ini import read_ini
url = read_ini()["host"]['api_sit_url']
@pytest.mark.parametrize("param", get_data["mobile_phone_belong"])
class TestMobile:
    def test_mobile_post(self, param):
        print("测试手机号 post 请求")
        r = requests.post(
            url=url + "/shouji/query",
            params={
                "shouji": param["shouji"],
                "appkey": param["appkey"]
            }
        )
        # 打印或处理响应
        print(r.json())