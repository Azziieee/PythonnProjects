import requests
import os
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "1ec2291f1c6ef67fd106e37a87ec7f0c"
account_sid = "AC605a3961bc80120824e6b41d9bed0012"
auth_token = "0bae4027e41793131732aa798e6b3bf3"

weather_params = {
    "lat": 17.361719,
    "lon": 79.475166,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
response = requests.get(OWN_Endpoint,params=weather_params)

response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+12562910679',
        to='+96878541061'
    )
print(message.status)


