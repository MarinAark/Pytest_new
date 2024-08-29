import requests

# 创建一个会话
req = requests.Session()
url = "http://sellshop.5istudy.online/sell/user/login"

data = {
    "username": "test01",
    "password": 123456
}
# 登陆，req保存了cookie或者 session
res = req.post(url, data=data)     # 登陆使用 post 请求， 查询使用 get 请求
# print(res.status_code)
# print(res.text)

url2 = "http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10"
res2 = req.get(url2)
# print(res2.status_code)
# print(res2.text)

# 写法二：
url = "http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10"
headers = {
    "token": "b94f22fc-d14b-492f-9e35-874bed392c04"
}
res3 = requests.get(url, headers=headers)
print(res3.status_code)
print(res3.text)