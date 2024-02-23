import requests
from datetime import datetime
from barer_token import barer_token

GENDER = "male"
WEIGHT_KG = 93
HAIGHT_CM = 191
AGE = 40

APP_ID = "89c37b11"
API_KEY = "5bb4cc6afbd1d181da1096800ad23a67"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = (
    "https://api.sheety.co/d0414b42a4f999c90157164e1271293e/workoutTracking/arkusz1"
)

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HAIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


####### https://docs.google.com/spreadsheets/d/1-wg8HxHUMRmlHPIH72kgCD3gvk47VYspo4VxGcCCIyc/edit#gid=0#########
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {"Authorization": f"Bearer {barer_token}"}


for exercise in result["exercises"]:
    sheet_inputs = {
        "arkusz1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
sheet_response = requests.post(
    sheet_endpoint, json=sheet_inputs, headers=bearer_headers
)
print(sheet_response.text)
