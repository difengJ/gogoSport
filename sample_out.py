import json

with open("./sample.json", "r") as fhand:
    js_obj = json.loads(fhand.read())
    # print(js_obj)
for item in js_obj["data"]["booking_array"]:
    tmp = item["booking_infos"][1]
    print(tmp["_field"], tmp["_time"], tmp["showTime"])


# 5fbb0cda7fe02a13460efc0b 5fbb0d21a9a781134040a015 07:00--08:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e4618ed3b12b37ff051 08:00--09:00
# 5fbb0cda7fe02a13460efc0b 5fbb0dfdc3f5a10ff4a5f161 09:00--10:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e11937aa712a8c227d8 10:00--11:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e26c3f5a10ff4a5f16e 11:00--12:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e36c3f5a10ff4a5f177 12:00--13:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e5947c6f60ffbd984a5 13:00--14:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e668c9b4d124058551c 14:00--15:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e70937aa712a8c227e1 15:00--16:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e8147c6f60ffbd984ae 16:00--17:00
# 5fbb0cda7fe02a13460efc0b 5fbb0e8d7fe02a13460efc12 17:00--18:00
# 5fbb0cda7fe02a13460efc0b 5fbb0ea847c6f60ffbd984b7 18:00--19:00
# 5fbb0cda7fe02a13460efc0b 5fbb0eb447c6f60ffbd984c0 19:00--20:00
# 5fbb0cda7fe02a13460efc0b 5fbb0ec13174ad1246395acc 20:00--22:00