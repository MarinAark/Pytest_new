import requests

json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

r = requests.post(url="https://jsonplaceholder.typicode.com/posts", json=json_data)
print(f'手机号码用例返回的状态码是：{r.status_code}')
print(f'手机号码用例返回的json数据是：{r.json()}')


print("\n--------这是一条分隔符---------\n")

data = {
    "text": "hello,world"
}
r2 = requests.post(url="https://dict.youdao.com/keyword/key", data=data)
print(f'有道用例的返回码是：{r2.status_code}')
print(f'有道用例返回的文本内容是：{r2.text}')
