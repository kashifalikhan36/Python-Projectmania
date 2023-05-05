#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_search=FlightSearch()
data=DataManager()

# for i in range(2,12):
#     city_name=data.give(i)['city']
#     iata_name=flight_search.get_destination_code(city_name)
#     price=flight_search.flight_search(i)
#     data.add_test(i,iata_name,price)


flight_data=FlightData()