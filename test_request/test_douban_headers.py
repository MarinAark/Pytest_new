import requests

url = 'https://movie.douban.com/j/search_subjects'
params = {
    "type": "movie",
    "tag": "$E7%83%AD%E9%97%A8",
    "page_limit": 20,
    "page_start": 0
}

headers = {
"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
}

r = requests.get(url=url, params=params, headers=headers)
print(r.status_code)
print(r.json())     # 返回码 418 ，反爬程序，解决方法，get请求，加上请求头
print(r.text)
