import requests
from datetime import datetime

USERNAME = "roki23232"
TOKEN = "sfdsd232342342f"
GRAPH_ID = "graph1"

pixela_enpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response1 = requests.post(url=pixela_enpoint, json=user_params)
# print(response1.text)


graph_enpoint = f"{pixela_enpoint}/{USERNAME}/graphs"
graph_param = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=graph_enpoint, json=graph_param, headers=headers)
# print(response.text)

pixel_enpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}
pixel_response = requests.post(url=pixel_enpoint, json=pixel_param, headers=headers)
print(pixel_response.text)


# update_enpoint = f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_param = {"quantity": "15.0"}
# update_request = requests.put(url=update_enpoint, json=new_pixel_param, headers=headers)
# print(update_request.text)

# delete_enpoint = (
#     f"{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# )

# delete_response = requests.delete(url=delete_enpoint, headers=headers)
# print(delete_response.text)
