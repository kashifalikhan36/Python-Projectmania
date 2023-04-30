import requests
from flight_search import FlightSearch

SHEETY_API_ENDPOINTS="https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeals/prices"
sheety_header={"Authorization":"Basic a2FzaGlmOkFxdWF0eXBlMQ=="}
cities=['NYC', 'PAR', 'LON', 'TYO', 'ROM', 'SYD', 'LAX', 'BCN', 'BER', 'AMS', 'DXB', 'IST', 'SIN', 'HKG', 'BKK', 'RIO', 'CAI', 'ATH']

class FlightData:
    def __init__(self):
        self.data={}
        for city in cities:
            
            self.flight_response=FlightSearch(city=city)
            self.flight=self.flight_response.data_send()
            if self.flight["data"][0]:
                self.iata_to=self.flight["data"][0]["flyTo"]
                self.price=self.flight["data"][0]["price"]
                self.city_to=self.flight["data"][0]["cityTo"]

                self.data[self.city_to]=self.price
                
                
                self.sheety_config = {
                "price":{
                    "city": self.city_to,
                    "iataCode": self.iata_to,
                    "lowestPrice": self.price
                }
            }
                print(self.sheety_config)
                self.response_sheety = requests.post(url=SHEETY_API_ENDPOINTS, json=self.sheety_config,headers=sheety_header)
                print(self.response_sheety.text)
                #This class is responsible for structuring the flight data and talking to the Google Sheet.
        
    def list_of_collected_data(self):
        return self.data