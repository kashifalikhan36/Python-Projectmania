import requests
import datetime
import smtplib

MY_LAT = 26.449923 # Your latitude
MY_LONG = 80.331871 # Your longitude
my_email = "itnajitna@gmail.com"
passw = "imwfxsmrztktngjh"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data_1 = response.json()
sunrise = data_1["results"]["sunrise"].split("T")[1].split(":")
sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])
time_sunrise= datetime.time(int(sunrise[0]),int(sunrise[1]),int(sunrise[2]))
time_sunset= datetime.time(int(sunset[0]),int(sunset[1]),int(sunset[2]))
time_now = datetime.datetime.now().time()
print(time_now)
#If the ISS is close to my current position
if 75.0<=float(data_1["iss_position"]['longitude'])<=85.0 and 20.0<=float(data_1["iss_position"]['latitude'])<=30.0:
    if time_now>=time_sunrise:
        ms="it is currently bright."
    elif time_now>=time_sunset:
        ms="it is currently dark."
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kashifalikhan093@gmail.com",
            msg=f"Subject:Look up in Sky !!!\n\nThe International Station is there and {ms}"
        )

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.