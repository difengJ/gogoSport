import json
import requests
import datetime


def get_1_day_free_field(item_datetime, item_timestamp):
    free_fields = []
    url = "https://field.hulasports.com/api/orderlists/get/book"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(
        {
            "orderDateNum": item_timestamp,
            "_venue": "59cc969742fa6b6703843bbe",
            "_item": "5fbb0b6f47c6f60ffbd98483",
            "passBaseOn": "start",
            "showLine": "row",
            "showPassTime": False,
            "_org": "59cb5c718e1e92a702eca340",
            "delayMins": 0,
        }
    )
    proxies = {
        "http": "http://hk1.dav2.top:14444",
        # "https": "http://10.10.1.10:1080",
    }
    res = requests.post(url, headers=headers, data=payload, proxies=proxies)
    booking_array = res.json()["data"]["booking_array"]
    for bookings in booking_array:
        for booking in bookings["booking_infos"]:
            if (
                booking["state"]["state"] == "可预订"
                and booking["_time"] != "07:00--08:00"
            ):
                free_fields.append(
                    (
                        item_datetime,
                        item_timestamp,
                        booking["_field"],
                        booking["_time"],
                        booking["fieldName"],
                        booking["showTime"],
                    )
                )
    return free_fields


def get_7_day_free_field():
    today = datetime.date.today()
    today_7days = []
    for i in range(8):
        today_7days.append(today + datetime.timedelta(days=i))
    today_7days_timestamp = [
        (item, int(item.strftime("%s")) * 1000) for item in today_7days
    ]
    for item in today_7days_timestamp:
        print(get_1_day_free_field(item[0], item[1]))


if __name__ == "__main__":
    get_7_day_free_field()