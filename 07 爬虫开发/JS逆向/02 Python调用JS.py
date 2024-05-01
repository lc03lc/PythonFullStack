import execjs
import requests

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': 1,
    'num': 20,
    'unionid': ''
}

j = requests.post(url, data=data, headers=headers).json()
encrypt_data = j['encrypt_data']

with open('./Python调用JS.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

result = execjs.compile(jscode).call('s', encrypt_data)

print(result)

