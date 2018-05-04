import requests
url = 'http://m.imooc.com/passport/user/login'
data = {
    "username":"18513199586",
    "password":"111111",
    "verify":"",
    "referer":"https://m.imooc.com"
}

res = requests.post(url,data).json()
# print(res)
# print(res['data']['url'][0])
response_url = res['data']['url'][0]

request_url = response_url + '&callback=jQuery19108043900278724099_1525401884932&_=1525401884935'
cookie = requests.get(request_url).cookies
cookie = requests.utils.dict_from_cookiejar(cookie)
print(cookie)

