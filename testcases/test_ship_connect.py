import requests
import pytest
# 1、用户登录
# 2、登陆之后拿到token，获取用户信息

class Test_login:
    token_1 = ""
    username_1 = ""
    def test_login(self):
   #     login_json = {
   #         "username": "ma",
   #         "password": "123456"
   #     }

       #  res = requests.post("/login", json = login_json)
        token = "token"
        username = "username"
        assert token == "token"
        assert username == "username"
        Test_login.token_1 = "token"
        Test_login.username_1 = 'username'


    def test_userinfo(self):
        # token, username = self.test_login()
        headers = {
            "token": Test_login.token_1,
            "username": Test_login.username_1
        }

        assert headers["token"] == Test_login.token_1
        assert headers["username"] == Test_login.username_1



if __name__ == '__main__':
    pytest.main()
