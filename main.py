import requests

url = "https://api.go-sports.cn/home/dateListNew"

payload = "venue_id=1&field_type=out&field_id=0&undefined="
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
    'Content-Type': "application/x-www-form-urlencoded",
    'Host': "api.go-sports.cn",
    'ua': "i|macOS 10.14.6|3.0|ql_gg||375|667|0|3145|1615044561|0c6313c66497f303076af9cc9f0d1788|75067eb24338ae66d403ed0a818e8df9|MacBookPro12,1",
    'cache-control': "no-cache",
    'Postman-Token': "639d0627-0e9d-426e-99e3-ae806f6131d7"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
