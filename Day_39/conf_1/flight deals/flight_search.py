import requests

FLIGHT_API_ENDPOINT="https://api.tequila.kiwi.com/v2/search"
flight_header={
    "apikey":"QvpJfeP3woCaaV50Toywqywoj14v69Xi"
               }
TEQUILA_ENDPOINT="https://api.tequila.kiwi.com/v2/search"

class FlightSearch:

    def __init__(self,city):

        self.flight_config={
        "fly_from":"DEL",
        "fly_to":city,
        "dateFrom":"30/04/2023",
        "dateTo":"30/12/2023",
        "curr":"GBP",
        "price_from":10,
        "price_to":900
    }
        
        
    def data_send(self):
        self.response=requests.get(url=FLIGHT_API_ENDPOINT,headers=flight_header,params=self.flight_config)
        return self.response.json()
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
            query = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }

            response = requests.get(
                url=FLIGHT_API_ENDPOINT,
                headers=flight_header,
                params=query,
            )
            
            try:
                data = response.json()["data"][0]
            except :
                print(f"No flights found for {destination_city_code}.")
                return None
            print(data)
            self.flight_data={
                "price":data["price"],
                "origin_city":data["route"][0]["cityFrom"],
                "origin_airport":data["route"][0]["flyFrom"],
                "destination_city":data["route"][0]["cityTo"],
                "destination_airport":data["route"][0]["flyTo"],
                "out_date":data["route"][0]["local_departure"].split("T")[0],
                "return_date":data["route"][1]["local_departure"].split("T")[0]
                }
            print(f"{self.flight_data.destination_city}: £{self.flight_data.price}")
            return self.flight_data
    

    #This class is responsible for talking to the Flight Search API.