import datetime
import requests
parameters={
    "lat":26.449923,
    "lng":80.331871,
    "formatted":0
}
data={}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters).json()
sunrise=response['results']['sunrise']
sunset=response['results']['sunset']
sunrise_text=f'{sunrise.split("T")[0]} {sunrise.split("T")[1].split("+")[0]}'
print(sunrise_text)
print(datetime.datetime.now())