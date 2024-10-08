import requests
import pytest





class Test_mobile:
    def setup_class(self):
        print("准备测试数据")

    def teardown_class(self):
        print("清理测试数据")


    def test_mobile_post(self):
      #   print("测试手机号post请求")
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


    def test_mobile_get(self):
    #    print("测试手机号get请求")
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
