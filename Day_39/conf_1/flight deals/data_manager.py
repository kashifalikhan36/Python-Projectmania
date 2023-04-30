import requests
SHEETY_API_ENDPOINTS="https://api.sheety.co/e6547815e2c372f77cae4ea1b0593714/flightDeals/prices"
sheety_header={"Authorization":"Basic a2FzaGlmOkFxdWF0eXBlMQ=="}

class DataManager:
    def __init__(self):
        pass
    def input_price(self,config,id):
            requests.put(url=f"{SHEETY_API_ENDPOINTS}/{id}",headers=sheety_header,json=config)

    def pass_end_data(self):
         return requests.get(url=SHEETY_API_ENDPOINTS,headers=sheety_header)
    #This class is responsible for talking to the Google Sheet.