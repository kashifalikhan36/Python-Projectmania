import requests
SHEETY_API_ENDPOINTS="https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeal/prices"
SHEETY_API_ENDPOINTS_EMAILS = "https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeal/emails"
sheety_header={"Authorization":"Basic a2FzaGlmOkFxdWF0eXBlM"}

class DataManager:
    def __init__(self):
        pass
        
    def add_test(self,i,iata_name,price):
        sheety_confg={
    "price":{
    'iata':iata_name,
    'lowest':price
    }
}
        self.response_sheety = requests.put(url=f"{SHEETY_API_ENDPOINTS}/{i}",headers=sheety_header,json=sheety_confg)

    def give(self,i):
        self.response_sheety = requests.get(url=f"{SHEETY_API_ENDPOINTS}/{i}",headers=sheety_header)
        return self.response_sheety.json()['price']
    def all_data(self):
        self.response_sheety = requests.get(url=f"{SHEETY_API_ENDPOINTS}",headers=sheety_header)
        return self.response_sheety.json()['prices']
    def send_email_data(self):
        self.response_sheety = requests.get(url=f"{SHEETY_API_ENDPOINTS_EMAILS}",headers=sheety_header)
        return self.response_sheety.json()['emails']

    #This class is responsible for talking to the Google Sheet.