import requests
import os
from twilio.rest import Client
from twil import sms

account= sms.account_sid
token= sms.auth_token
api=sms.api_key

account_sid = account
auth_token = token



latitude=54.516842
longitude=18.541941
api_key = api
enpoint= "https://api.openweathermap.org/data/2.5/forecast"
weather_parameters={
    "lat":latitude,
    "lon":longitude,
    "appid":api_key,
    "units":"metric",
    "cnt":4,
}
response=requests.get(enpoint,params=weather_parameters)
# response.raise_for_status()
weather_data=response.json()
# print(weather_data)

will_rain=False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True
if will_rain == True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bedzie padało uważaj hehe !:)☂️",
        from_=sms.twilio_phone,
        to=sms.my_phone
    )
    print(message.status)





