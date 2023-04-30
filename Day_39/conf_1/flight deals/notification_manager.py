from twilio.rest import Client
account_sid ="ACc97d07942975958296f11ef0697129bd"
auth_token ="c7765cd1effe6b95acc565ad2a50eeb8"
class NotificationManager:
    def __init__(self):
        pass

    def send_msg(self,data):
        self.client = Client(account_sid, auth_token)
        self.message = self.client.messages \
                        .create(
                            body=data,
                            from_='+16206048278',
                            to='+916306868361'
                        )

        print(self.message.status)
#This class is responsible for sending notifications with the deal flight details.