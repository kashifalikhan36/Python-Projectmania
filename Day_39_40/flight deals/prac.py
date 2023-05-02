# import requests
# from datetime import datetime,timedelta
# import pprint
# from notification_manager import NotificationManager

# tommorow=datetime.now().date()+timedelta(days=1)
# six_month_later=datetime.now().date()+timedelta(days=6*30)
# TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
# TEQUILA_API_KEY = "QvpJfeP3woCaaV50Toywqywoj14v69Xi"

# notify=NotificationManager()

# headers = {"apikey": TEQUILA_API_KEY}
# city="DPS"
# query={
#             "fly_from":"LON",
#             "fly_to":city,
#             "date_from":tommorow.strftime("%d/%m/%Y"),
#             "date_to":six_month_later.strftime("%d/%m/%Y"),
#             "nights_in_dst_from": 7,
#             "nights_in_dst_to": 28,
#             "flight_type": "round",
#             "one_for_city": 1,
#             "max_stopovers": 5,
#             "price_from":0,
#             "price_to":1000
#         }
# temp = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=query).json()
# price=temp['data'][0]['price']
# cityFrom=temp['data'][0]['cityFrom']
# cityCodeFrom=temp['data'][0]['cityCodeFrom']
# cityTo=temp['data'][0]['cityTo']
# out_date=temp['data'][0]["route"][0]["local_departure"].split("T")[0],
# return_date=temp['data'][0]["route"][1]["local_departure"].split("T")[0]
# flight_over_no=0
# flight_city=''
# while True:
#    cityCodeTo=temp['data'][0]['route'][flight_over_no]['cityCodeTo']
#    cityTo=temp['data'][0]['route'][flight_over_no]['cityTo']
#    if temp['data'][0]['route'][flight_over_no]['cityCodeTo']==city:
        
#         if flight_over_no==0:
#             flight_city=f" {cityTo}-{cityCodeTo}"
#         elif flight_over_no>0:
#             flight_city+=f" {cityTo}-{cityCodeTo} "
#         print('okay lets go another city')
#         print(city)
#         cityCodeTo=temp['data'][0]['cityCodeTo']
#         break
   
       
#    elif temp['data'][0]['route'][flight_over_no]['cityCodeTo']!=city:
#         if  flight_over_no==0:
#             flight_city+=f" {cityTo}-{cityCodeTo}"
#         else:
#             flight_city+=f" Then {cityTo}-{cityCodeTo}"
#         flight_over_no+=1
#         print(flight_over_no)
# flight_over_no
# print(f"{price,cityFrom,cityCodeFrom,cityTo,cityCodeTo,out_date,return_date} with the flight over no.{flight_over_no} , the Flight over City :- {flight_city}")


# import requests

# SHEETY_API_ENDPOINTS_EMAILS = "https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeal/emails"
# sheety_header = {"Authorization": "Basic a2FzaGlmOkFxdWF0eXBlMQ=="}

# response_sheety = requests.get(url=f"{SHEETY_API_ENDPOINTS_EMAILS}",
#                                   headers=sheety_header)
# print(response_sheety.json())
# import smtplib

# my_email = "itnajitna@gmail.com"
# passw = "imwfxsmrztktngjh"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=passw)
#     connection.sendmail(
#     from_addr=my_email,
#     to_addrs=["kashifalikhan093@gmail.com", "kashifalikhan78677868@gmail.com"],
#     msg=f"Low Flight Price Alert !!!\n\nLow Price Alert !!! Only :")