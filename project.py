import requests

from datetime import datetime

api_key= " 87d845b0b6cf29baa1a73cc34b067a95 "
location=input("Enter Your City:")

complete_link="api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

link=requests.get(complete_link)
data=link.json()


weather=data["weather"][0]["description"]
hmdt=data["main"]["humidity"]
wind_speed=data["wind"]["speed"]
date=datatime.now().strtime("%d %b %Y  |  %I:%M:%S %p " )

print("Weather stauts for -{}  || {}".format(location.upper(),datatime))

print("Current Weather desc = ",weather)
print("Current Humadity=",hmdt, "%")
print("Current wind speed= ",wind_speed)