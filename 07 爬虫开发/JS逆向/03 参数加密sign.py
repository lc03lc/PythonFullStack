import requests
import time
import execjs
import json

url = 'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    'referer': 'https://sale.1688.com/',
    'cookie': 'cna=ySvwGqQdOVICAQ5ssN9/6KXi; _m_h5_tk=39415c4a4dd8fb21379f89a700b0ef7a_1662005910055; _m_h5_tk_enc=2b59a79a27f8be7823d7fbe43a0938a2; cookie2=1eb4072fb22e1dd573afad905f347421; t=2680111738ff8e4299b79a83c1b89870; _tb_token_=1e3eee8b6373; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1661996913193; isg=BGBg2Z_bF7OD86uqCTNMTrCfMW4yaUQzjMLrEdpxG3sO1QH_gnqWw6mkbX3V5fwL; l=eBgCunpnTgbVDxTJBOfwlurza77tvIRfguPzaNbMiOCP9p1M5YaCW6kxNSYHCnGVnsH2R3klB_F6ByTa5yUIQxv9-egqiji_CdTh.; tfstk=cBx1Bqw425V14ScCTNMEuT5z8PjPaBgCpV1eCXXzNNVjlc9h9sx44_9E_EVC0tBC.'
}

# j = h(d.token + "&" + i + "&" + g + "&" + c.data)
token = '39415c4a4dd8fb21379f89a700b0ef7a'
i = round(time.time() * 1000)
g = "12574478"
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\",\\"url\\":\\"https://sale.1688.com/factory/category.html\\"}"}'


with open('./参数加密.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
signKey = token + "&" + str(i) + "&" + g + "&" + data
sign = execjs.compile(jscode).call('h', signKey)
print(sign)

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': i,
    'sign': sign,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': 0,
    'timeout': 20000,
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc3',
    # 'data': '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\"query\":\"mainCate=&leafCate=\",\"sort\":\"mix\",\"pageNo\":\"1\",\"pageSize\":\"20\",\"from\":\"PC\",\"trafficSource\":\"pc_index_recommend\",\"url\":\"https://sale.1688.com/factory/category.html\"}"}'
    'data': data
}

res = requests.get(url, headers=headers, params=params).text[18:-1]

j = json.loads(res)
with open('1688.json', 'w', encoding='utf-8') as f:
    json.dump(j, f, ensure_ascii=False, indent=4)
