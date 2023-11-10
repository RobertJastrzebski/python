import time
import requests
from datetime import datetime



MY_LAT= 54.516842 #My latitude
MY_LONG= 18.541941 #My longitude


def is_iss_overhead():
    # Checks If the ISS is close to my current position
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])


    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night_time():
    #checks if it is currently dark
     parameters = {
         "lat": MY_LAT,
         "lng": MY_LONG,
         "formatted": 0,
     }
     response= requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
     response.raise_for_status()
     data= response.json()

     sunrise =int(data["results"]["sunset"].split("T")[1].split(":")[0])
     sunset =int(data["results"]["sunrise"].split("T")[1].split(":")[0])

     time_now = datetime.now().hour

     if time_now >= sunrise or time_now <= sunset:
         return True




def iss_above_me_check():
    # function check and tell me to look up.
    if is_iss_overhead() and is_night_time():
        print("Look up Iss is above you")
    else:
        print("Iss is not above you right know")


while True:
    time.sleep(60)
    iss_above_me_check()


