import re
import requests
import json
import datetime
import time


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


url = "https://field.hulasports.com/api/orderlists/get/book"

today = datetime.date.today()
today_7days = []
for i in range(8):
    today_7days.append(today + datetime.timedelta(days=i))

today_7days_timestamp = [
    (item, int(item.strftime("%s")) * 1000) for item in today_7days
]
headers = {"Content-Type": "application/json"}
# wanted_time_list = []
message = ""
for item_datetime, item_timestap in today_7days_timestamp:
    payload = json.dumps(
        {
            "orderDateNum": item_timestap,
            "_venue": "59cc969742fa6b6703843bbe",
            "_item": "5fbb0b6f47c6f60ffbd98483",
            "passBaseOn": "start",
            "showLine": "row",
            "showPassTime": False,
            "_org": "59cb5c718e1e92a702eca340",
            "delayMins": 0,
        }
    )
    res = requests.post(url, headers=headers, data=payload)
    booking_array = res.json()["data"]["booking_array"]
    for bookings in booking_array:
        for booking in bookings["booking_infos"]:
            if (
                booking["state"]["state"] == "可预订"
                and booking["showTime"] != "07:00--08:00"
                and booking["showTime"] != "08:00--09:00"
            ):
                message += "%s,%s,%s\n" % (
                    item_datetime,
                    booking["fieldName"],
                    booking["showTime"],
                )
print(message)
if len(message) == 0:
    print("没有适合的场地")
else:
    print(send_message(message))