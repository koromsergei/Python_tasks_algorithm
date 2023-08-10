import requests
import time

session = requests.Session()
url = 'https://gorzdrav.spb.ru/_api/api/v2/schedule/lpu/315/doctor/16/appointments'

while True:
    res = session.get(url)
    print(res.json()["success"])
    time.sleep(10)
