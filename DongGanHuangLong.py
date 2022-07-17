import requests
import json
import datetime
from CheckFreeField import get_1_day_free_field
import hashlib


def send_message(message):
    # url = "https://sctapi.ftqq.com/SCT159529TUnz8UvsyAvX0PtokeG8Bq7CQ.send"
    url = "http://wxpusher.zjiecode.com/api/send/message"
    # payload = {"title": "动感黄龙场地监控", "desp": message, "channel": 9}
    payload = {
        "appToken": "AT_p20fCGhiGWmz81dRCjdewu2STgccvaWw",
        "content": message,
        "summary": "动感黄龙场地监控",
        "contentType": 1,
        "uids": ["UID_qAKttHJKCymkQTMzS2R3Vjk4TF4g"],
        "url": "http://wxpusher.zjiecode.com",
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=payload, headers=headers)
    return res.text


def make_order(orderDate, field, time):
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(
        {
            "_org": "59cb5c718e1e92a702eca340",
            "_member": "5f349f902247cbac77c48fc3",
            "openid": "o75LU5KjjInFmf-i5KVvalk_JQZw",
            "orderDate": orderDate,
            "orderArr": [
                {
                    "_field": field,
                    "_time": time,
                }
            ],
            "payment": "member",
            "state": "xiaochengxu",
            "thirdName": "微信",
            "randomStr": "pHfHRfNNiEWxe",
            "sign": "521ba84118c0e13e643688a7279b49f6",
        }
    )
    url = "https://field.hulasports.com/api/orderlists/pay/bail"
    url = "https://field.hulasports.com/api/orderlists/orders"
    res = requests.post(url, headers=headers, data=payload)
    print(res.text)


def hash_md5(s):
    res = s
    h1 = hashlib.md5()
    h1.update(res.encode(encoding="utf-8"))
    return h1.hexdigest()


def getsign(dic):
    s = str()
    for i in sorted(dic):
        s += i + str(dic[i])
    return hash_md5(s)


if __name__ == "__main__":
    today = datetime.date.today()
    today_after_7_day = today + datetime.timedelta(days=7)
    today_after_7_day_num = int(today_after_7_day.strftime("%s")) * 1000
    # print(today_after_7_day, today_after_7_day_num)
    free_field = get_1_day_free_field(today_after_7_day, today_after_7_day_num)
    print(free_field[0][1], free_field[0][2], free_field[0][3])
    make_order(free_field[0][1], free_field[0][2], free_field[0][3])
