import requests
import pytest


# 默认scop是function
@pytest.fixture(scope="class")
def func():
    print("这是测试前置步骤")


def test_mobile_post1(func):
    print("class外部，测试手机号post请求1")
    r = requests.post(url="http://api.binstd.com/shouji/query", params={
        "shouji": "13456755448",
        "appkey": "0c818521d38759e1"})


    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == 'ok'
    assert result["result"]["shouji"] == "13456755448"
    assert result["result"]["province"] == "浙江"
    assert result["result"]["city"] == "杭州"
    assert result["result"]["company"] == "中国移动"
    assert result["result"]["areacode"] == "0571"

mobile = "10291921"


class Test_fixture:
    def test_mobile_post(self, func):
        print("class类中，测试手机号post请求1")
        r = requests.post(url="http://api.binstd.com/shouji/query", params={
            "shouji": "13456755448",
            "appkey": "0c818521d38759e1"})

        assert r.status_code == 200
        result = r.json()
        assert result["status"] == 0
        assert result["msg"] == 'ok'
        assert result["result"]["shouji"] == "13456755448"
        assert result["result"]["province"] == "浙江"
        assert result["result"]["city"] == "杭州"
        assert result["result"]["company"] == "中国移动"
        assert result["result"]["areacode"] == "0571"

 #    @pytest.mark.skipif('len(mobile)!=2')
    def test_mobile_get(self, func):
        print("class类中，测试手机号get请求1")
        r = requests.get(url="http://api.binstd.com/shouji/query", params={
            "shouji": "13456755448",
            "appkey": "0c818521d38759e1"})

        assert r.status_code == 200
        result = r.json()
        assert result["status"] == 0
        assert result["msg"] == 'ok'
        assert result["result"]["shouji"] == "13456755448"
        assert result["result"]["province"] == "浙江"
        assert result["result"]["city"] == "杭州"
        assert result["result"]["company"] == "中国移动"
        assert result["result"]["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
