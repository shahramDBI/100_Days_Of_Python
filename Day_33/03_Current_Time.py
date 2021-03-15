import requests
from datetime import datetime

My_Lat = 35.715298
My_Long = 51.404343

parameters = {
    "lat": My_Lat,
    "lng": My_Long,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(data)
print(sunrise.split("T")[1].split(":")[0])
print(sunset)
time_now = datetime.now()
print(time_now)