# import requests
# MY_LAT = 26.449923 # Your latitude
# MY_LONG = 80.331871 # Your longitude
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data_1 = response.json()
# sunrise = data_1["results"]["sunrise"].split("T")[1].split(":")
# sunset = data_1["results"]["sunset"].split("T")[1].split(":")
# print(sunset[2][0]+sunset[2][1])

#Used for tests