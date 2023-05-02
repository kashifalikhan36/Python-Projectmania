from twilio.rest import Client
import smtplib

my_email = "itnajitna@gmail.com"
passw = "imwfxsmrztktngjh"

account_sid ="ACc97d07942975958296f11ef0697129bd"
auth_token ="c7765cd1effe6b95acc565ad2a50eeb8"

class NotificationManager:
    def __init__(self):
        pass

    def send_sms(self,price,from_city,from_city_iata,to_city,to_city_iata,date_from,date_to,flight_over_no,flight_city):
        self.client = Client(account_sid, auth_token)
        self.message = self.client.messages \
                        .create(
                            body=(f"Low Price Alert !!! Only £:{price} to fly from {from_city} - {from_city_iata} to {to_city} - {to_city_iata}, from {date_from} - {date_to}. And Flight has {flight_over_no} stop over, via {flight_city}"),
                            from_='+16206048278',
                            to='+916306868361'
                        )
        print(self.message.status)
    def send_mail(self,price,from_city,from_city_iata,to_city,to_city_iata,date_from,date_to,flight_over_no,flight_city,emails):
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=passw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=emails,
                msg=f"Subject:Low Flight Price Alert !!!\n\nLow Price Alert !!! \nOnly £:{price} to fly from {from_city} - {from_city_iata} to {to_city} - {to_city_iata}, \nFrom {date_from} - {date_to}. \nAnd Flight has {flight_over_no} stop over, via {flight_city}".encode('utf-8')
                )
        

#This class is responsible for sending notifications with the deal flight details.