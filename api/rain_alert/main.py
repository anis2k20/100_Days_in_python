import requests
from twilio.rest import Client

account_sid = 'AC1e0a91cc0ebdda61b97b5449853b79d7'
auth_token = '5c18b2047e029199f7742e6949edc34d'

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "46fd05732d818836b551ffe68affe58a"
weather_params = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
data = response.json()
print(data)

client = Client(account_sid, auth_token)

message = client.messages.create(
  body="This is test message",
  from_='+14342803111',
  to='+8801614637972'
)
print(message.status)
