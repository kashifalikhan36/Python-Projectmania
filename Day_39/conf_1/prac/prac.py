import requests
from datetime import datetime, timedelta

FLIGHT_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
flight_header = {
    "apikey": "QvpJfeP3woCaaV50Toywqywoj14v69Xi"
}
# flight_config = {
#     "fly_from": "DEL",
#     "fly_to": "LGA",
#     "dateFrom": "30/05/2023",
#     "dateTo": "30/12/2023",
#     "curr": "USD",
#     "price_from": 0,
#     "price_to": 700,
#     "asc": 1
# }
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# query = {
#     "fly_from": "DEL",
#     "fly_to": "LGA",
#     "date_from": tomorrow.strftime("%d/%m/%Y"),
#     "date_to": six_month_from_today.strftime("%d/%m/%Y"),
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#     "flight_type": "round",
#     "one_for_city": 1,
#     "max_stopovers": 0,
#     "curr": "USD"
# }

cities=['NYC', 'PAR', 'LON', 'TYO', 'ROM', 'SYD', 'LAX', 'BCN', 'BER', 'AMS', 'DXB', 'IST', 'SIN', 'HKG']
for city in cities:
    flight_config={
            "fly_from":"DEL",
            "fly_to":city,
            "dateFrom":"30/04/2023",
            "dateTo":"30/12/2023",
            "curr":"GBP",
            "price_from":10,
            "price_to":900
        }
response=requests.get(url=FLIGHT_API_ENDPOINT,headers=flight_header,params=flight_config)
print(response.json())
# response = requests.get(
#     url=FLIGHT_API_ENDPOINT,
#     headers=flight_header,
#     params=query,
# )

# print(response.json())
# k=0
# iata=response.json()["data"][0]["flyTo"]
# city=response.json()["data"][0]["cityTo"]
# price=response.json()["data"][0]["price"]
