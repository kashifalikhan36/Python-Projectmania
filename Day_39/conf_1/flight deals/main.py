#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

manager=DataManager(tomorrow,six_month_from_today)
notify=NotificationManager()
data_flight=FlightData()

min_dict=[]
min_city=""
data=manager.pass_end_data().json()['prices']
for temp_data in data:
    min_dict.append(temp_data['lowestPrice'])
for flight in data:
    if flight['lowestPrice'] == min(min_dict):
        min_city=flight['city']
        min_city=flight["route"][0]["flyFrom"]


# for destination in data:
flight = data_flight.search(
        'DEL',
        min_city,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
print(flight)
notify.send_msg(data=f"Low price alert!!! - Only  £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city} - {flight.destination_airport}, from {flight.out_date} to {flight.return_date}")