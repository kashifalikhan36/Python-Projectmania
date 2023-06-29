import requests
from datetime import datetime

USERNAME="kashif99"
TOKEN="token"
pixela_endpoints="https://pixe.la/v1/users"

user_prams={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoints,json=user_prams)
# print(response.text)

graph_endpoint=f"{pixela_endpoints}/{USERNAME}/graphs"

graph_config={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

header={
        "X-USER-TOKEN":TOKEN,
}

add_pixel_endpoint=f"{pixela_endpoints}/{USERNAME}/graphs/graph1"
yestarday=datetime(year=2023,month=4,day=26)
today=datetime.now()
pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many km u had traveltoday through marine cycle:-")
}

# response=requests.post(url=add_pixel_endpoint,json=pixel_config,headers=header)
# print(response.text)
config="%Y%m%d"
pixel_update_endpoint=f"/{USERNAME}/graphs/graph1/{yestarday.strftime(config)}"

pixel_update_config={
    "quantity":"40.23"
}

# response=requests.delete(url=f"{pixela_endpoints}/{pixel_update_endpoint}",json=pixel_update_config,headers=header)
# print(response.text)

response=requests.delete(url=f"{pixela_endpoints}/{pixel_update_endpoint}",headers=header)
print(response.text)