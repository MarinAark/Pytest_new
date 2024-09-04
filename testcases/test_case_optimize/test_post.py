import pytest
import requests
from utils.read import base_data
from api.api import mobile_query, T_json

url = "https://jsonplaceholder.typicode.com/posts"


def test_post():
    json_data = base_data.read_data()["json_data"]  # 直接获取字典
    result = T_json(json_data)
    assert result['id'] == 101
    # assert result['msg'] == 'ok'
    # assert result['result']['city'] == '杭州'
    # assert result['result']['province'] == '浙江'


if __name__ == '__main__':
    pytest.main()