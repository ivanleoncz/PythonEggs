#!/usr/bin/python3

import json
from urllib.request import urlopen

city = input("City: ")
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=b9f17f8103a7001e5d7c1296e202ab37" % city
response = urlopen(url).read().decode('utf-8')
data = json.loads(response)
#print(json.dumps(data,indent=2))
print("Temp Min.:",data["main"]["temp_min"])
print("Temp Max.:",data["main"]["temp_max"])

