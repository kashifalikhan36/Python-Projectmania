#API is now paid so this project is now gonna cancel today

import requests
from twilio.rest import Client
account_sid ="sid"
auth_token ="token"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Let's crack it!",
                     from_='+16206048278',
                     to='+916306868361'
                 )

print(message.status)
# parameters={
#     "lat":26.449923,
#     "lon":80.331871,
#     "appid":"17dd9e3e79a2764b66503f826869a84b",
#     "exclude":"current,minutely,daily"
# }
# MY_LAT = 26.449923 # Your latitude
# MY_LONG = 80.331871 # Your longitude
# response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
# response.raise_for_status()
# print(response.json())