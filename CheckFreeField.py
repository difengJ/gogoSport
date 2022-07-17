import json
import requests
import datetime
import random
from bs4 import BeautifulSoup as bs


def get_free_proxies():
    url = "https://www.beesproxy.com/free"
    headers = {"Content-Type": "application/json"}
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url, headers=headers).content, "html.parser")
    proxies = []
    for row in soup.find("table").find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
        # session = requests.Session()
        # session.proxies = {"http": host, "https": host}
        # if session.get("http://icanhazip.com", timeout=1.5).text.strip():
    return proxies


def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


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
    proxies = get_free_proxies()
    s = get_session(proxies)
    print(s.get("http://icanhazip.com", timeout=1.5).text.strip())
    res = s.post(url, headers=headers, data=payload)
    booking_array = res.json()["data"]["booking_array"]
    for bookings in booking_array:
        for booking in bookings["booking_infos"]:
            if (
                booking["state"]["state"] == "可预订"
                and booking["showTime"] != "07:00--08:00"
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