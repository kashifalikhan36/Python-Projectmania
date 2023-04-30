from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta

cities=['NYC', 'PAR', 'LON', 'TYO', 'ROM', 'SYD', 'LAX', 'BCN', 'BER', 'AMS', 'DXB', 'IST', 'SIN', 'HKG']
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

class FlightData:
    def __init__(self):
        self.manager=DataManager()
        self.data=[]
        self.id=2
        for city in cities:
            
            self.flight_response=FlightSearch(city=city)
            self.flight=self.flight_response.data_send()
            if self.flight["data"][0]:
                self.iata_to=self.flight["data"][0]["flyTo"]
                self.price=self.flight["data"][0]["price"]
                self.city_to=self.flight["data"][0]["cityTo"]
                
                self.sheety_config = {
                "price":{
                    "lowestPrice": self.price
                }
            }
                
                self.manager.input_price(self.sheety_config,self.id)
                self.id+=1
            
    def search(self,origin_city_code, destination_city_code, from_time, to_time):
        return self.flight_response.check_flights(origin_city_code, destination_city_code, from_time, to_time)


    #     self.data.append({
    #         self.data["price"]:self.new_data.price,
    #         self.data["origin_city"]:self.new_data.origin_city,
    #         self.data["origin_airport"]:self.new_data.origin_airport,
    #         self.data["destination_city"]:self.new_data.destination_city,
    #         self.data["destination_airport"]:self.new_data.destination_airport,
    #         self.data["out_date"]:self.new_data.out_date,
    #         self.data["return_date"]:self.new_data.return_date,
    #     })
    # def final_data(self):
    #     return self.data
                #This class is responsible for structuring the flight data and talking to the Google Sheet.