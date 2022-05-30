import os
import requests
from datetime import datetime
today = datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"
auth_token = "sakldjaksdsda"
USERNAME = "platypus567"
user_params = {
    "token": auth_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}


#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": auth_token
}
graph_params = {
    "id": "graph1",
    "name": "Code Tracking",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"

}
#response = requests.post(graph_endpoint,json=graph_params, headers=headers)
#print(response.text)

pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "220"

}
pixel_url = "https://pixe.la/v1/users/platypus567/graphs/graph1"
response = requests.post(url=pixel_url, json=pixel_params,headers=headers)
print(response.text)

#add put or delete for more formatting on graph, to see the graph go to https://pixe.la/v1/users/platypus567/graphs/graph1.html
