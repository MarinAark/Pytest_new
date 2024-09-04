import requests
import pytest
from utils.read import base_data
from api.api import mobile_query

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    param = base_data.read_data()["mobile_phone_belong"]  # 直接获取字典

    result = mobile_query(param)
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['city'] == '杭州'
    assert result['result']['province'] == '浙江'
