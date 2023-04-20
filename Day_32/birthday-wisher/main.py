import datetime
import smtplib
import random
import pandas
import math
texts=[]
my_email = "itnajitna@gmail.com"
passw = "imwfxsmrztktngjh"
data={row.names:[row.email,row.year,row.month,row.day] for index,row in pandas.read_csv("Day_32\\birthday-wisher\\birthdays.csv").iterrows()}
letters=["Day_32\\birthday-wisher\letter_templates\letter_1.txt","Day_32\\birthday-wisher\letter_templates\letter_2.txt","Day_32\\birthday-wisher\letter_templates\letter_3.txt"]

def emails_text():
    with open(random.choice(letters), mode="r") as file:
        return file.read()
    
def mail(text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kashifalikhan093@gmail.com",
            msg=f"Subject:Happy Birthday !!!\n\n{text}"
        )

for name in data:
    year=math.floor(data[name][1])
    month=math.floor(data[name][2])
    day=math.floor(data[name][3])
    check=datetime.date(year=year,month=month,day=day)
    if datetime.datetime.now()==check:
        text=emails_text().replace("[NAME]",name)
        mail(text)