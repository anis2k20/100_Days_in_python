import requests

MY_LNG = 90.356331
MY_LAT = 23.684994
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()

sun_rise = data["results"]["sunrise"]
print(sun_rise.split("T")[1].split(":")[0])

