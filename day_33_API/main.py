import requests

MY_LAT= "54.516842"
MY_LONG= "18.541941"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response= requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data=response.json()
print(data)

