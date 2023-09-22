import requests
from twisted.cred.credentials import UsernamePassword
from datetime import datetime

USERNAME = "anis2k20"
TOKEN = "jfhij345j344hjwkkw"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_insert_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# today = datetime(year=2023,month=9,day=21)
# graph_insert_params = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity": "1",
# }
#
# response = requests.post(url=graph_insert_endpoint, json=graph_insert_params,headers=headers)
# print(response.text)
graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230922"
pixel_data = {
    "quantity":"20",
}

response = requests.put(url=graph_put_endpoint, json=pixel_data, headers=headers)
print(response.text)
