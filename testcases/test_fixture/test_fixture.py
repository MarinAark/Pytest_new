import requests
import pytest


# 默认scop是function



def test_mobile_post1(test_func2, get_params):
    print("外部class，测试手机号post请求")
    r = requests.post(url="http://api.binstd.com/shouji/query", params=get_params)


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


class Test_mobile:
    def test_mobile_post(self, test_func, get_params):
        print("内部class，测试手机号post请求")
        r = requests.post(url="http://api.binstd.com/shouji/query", params=get_params)

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
    def test_mobile_get(self, get_params):
        print("内部class，测试手机号get请求")
        r = requests.get(url="http://api.binstd.com/shouji/query", params=get_params)

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
