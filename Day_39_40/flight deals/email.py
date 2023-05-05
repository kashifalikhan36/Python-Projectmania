import requests
from flight_data import FlightData

data=FlightData()

SHEETY_API_ENDPOINTS_EMAILS = "https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeal/emails"
sheety_header = {"Authorization": "Basic a2FzaGlmOkFxdWF0eXBlMQ=="}
print(
  "Welcome to the kashif's Flight \n we found the best flight deals and email u"
)
while True:
  first_name = input('What is ur first name? :-')
  last_name = input('What is ur last name? :-')
  email_input = input('What is ur email? :-')
  if email_input == input('Type ur email again? :-'):
    email = email_input
  else:
    print("Oops Type Again")
    continue
  sheety_confg = {
    "email": {
      'firstName': first_name,
      'lastName': last_name,
      'email': email
    }
  }
  response_sheety = requests.post(url=f"{SHEETY_API_ENDPOINTS_EMAILS}",
                                  headers=sheety_header,
                                  json=sheety_confg)
  if input('Do u want to add more emails ! type (Yes/No)').lower() == 'yes':
    break
  else:
    continue