from twilio.rest import Client
account_sid ="ACc97d07942975958296f11ef0697129bd"
auth_token ="c7765cd1effe6b95acc565ad2a50eeb8"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Let's crack it!",
                     from_='+16206048278',
                     to='+916306868361'
                 )

print(message.status)