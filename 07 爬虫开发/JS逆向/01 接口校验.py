import requests
import json

url = 'http://www.whggzy.com/front/search/category'

# headers需要在xhr断点中查找
headers = {
    'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_front.2ef5001f.0.0.8706ee7027ac11edb22bbd21980c6e27',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    'Accept': "*/*",
    'Content-Type': "application/json",
    'X-Requested-With': "XMLHttpRequest"
}

# data需要在xhr断点中查找
data = '{"utm": "sites_group_front.2ef5001f.0.0.8706ee7027ac11edb22bbd21980c6e27","categoryCode": "GovernmentProcurement","pageSize": 15,"pageNo": 1}'

response = requests.post(url=url, headers=headers, data=data)

j = json.loads(response.text)

with open('res.json', 'w') as f:
    json.dump(j, f, ensure_ascii=False, indent=2)


'''
检查以下问题：
接口问题， data问题， 请求方式问题
'''