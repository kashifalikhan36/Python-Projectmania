import smtplib
import datetime as dt
import random

my_email = "itnajitna@gmail.com"
passw = "imwfxsmrztktngjh"

def quots():
    data=open("Day_32\Monday_Motivation\quotes.txt",mode="r")
    list_quots=data.readlines()
    return random.choice(list_quots)

def mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passw)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="kashifalikhan093@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quots()}"
        )

data=dt.datetime.now().weekday()
if data==2:
    mail()

# now=dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()
# print(day_of_week)

# date_of_birth=dt.datetime(year=2004,month=8,day=12)
# print(date_of_birth)

