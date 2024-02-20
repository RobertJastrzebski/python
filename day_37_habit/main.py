import requests

pixela_enpoint= "https://pixe.la/v1/users"
user_params={
    "token": "roij3oij4oij",
    "username": "roki",
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_enpoint,json=user_params)
print(response)

