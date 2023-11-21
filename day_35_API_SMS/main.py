import requests

latitude=54.516842
longitude=18.541941
api_key = "a94728d0ae456b874c95b9a337899979"
enpoint= "https://api.openweathermap.org/data/2.5/weather"
weather_parameters={
    "lat":latitude,
    "lon":longitude,
    "appid":api_key,
    "units":"metric"
}
response=requests.get(enpoint,params=weather_parameters)
print(response.json())
# print(response.status_code)




