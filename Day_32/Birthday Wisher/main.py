# import smtplib

# my_email = "itnajitna@gmail.com"
# passw = "imwfxsmrztktngjh"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=passw)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="kashifalikhan093@gmail.com",
#         msg="Subject:Hello\n\nThis is body of email"
#     )
import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(day_of_week)

date_of_birth=dt.datetime(year=2004,month=8,day=12)
print(date_of_birth)