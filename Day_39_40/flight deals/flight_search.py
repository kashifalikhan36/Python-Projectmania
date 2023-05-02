import requests
from datetime import datetime,timedelta
from data_manager import DataManager
from notification_manager import NotificationManager

data=DataManager()
notify=NotificationManager()

tommorow=datetime.now().date()+timedelta(days=1)
six_month_later=datetime.now().date()+timedelta(days=6*30)
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API_KEY = "QvpJfeP3woCaaV50Toywqywoj14v69Xi"

class FlightSearch:
    def __init__(self):
        pass
    

    def get_destination_code(self, city_name):
        location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations'][0]['code']
        return results
    def search(self,city):
        headers = {"apikey": TEQUILA_API_KEY}
        if city=="DPS":
            query={
            "fly_from":"LON",
            "fly_to":city,
            "date_from":tommorow.strftime("%d/%m/%Y"),
            "date_to":six_month_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 5,
            "price_from":0,
            "price_to":1000
        }
        else:
            query={
            "fly_from":"LON",
            "fly_to":city,
            "date_from":tommorow.strftime("%d/%m/%Y"),
            "date_to":six_month_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "price_from":0,
            "price_to":1000
        }
        
        
        self.search_response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=query)
        return self.search_response.json()
    
    def flight_search(self,i):
        city_name=data.give(i)['iata']
        try: 
            city=self.search(city_name)['data'][0]['cityTo']
            price=self.search(city_name)['data'][0]['price']
        except(IndexError):
            print(f"No flights found for {city_name}.")
            return None
        print(f"{city} : GBP {price}")
        return price
    def flight_final_data_search(self,iata_city):
        try:
            temp=self.search(iata_city)
            price=temp['data'][0]['price']
            cityFrom=temp['data'][0]['cityFrom']
            cityCodeFrom=temp['data'][0]['cityCodeFrom']
            cityTo=temp['data'][0]['cityTo']
            out_date=temp['data'][0]["route"][0]["local_departure"].split("T")[0],
            return_date=temp['data'][0]["route"][1]["local_departure"].split("T")[0]
            flight_over_no=0
            flight_city=''
            while True:
                cityCodeTo=temp['data'][0]['route'][flight_over_no]['cityCodeTo']
                cityTo=temp['data'][0]['route'][flight_over_no]['cityTo']
                if temp['data'][0]['route'][flight_over_no]['cityCodeTo']==iata_city:
                        
                        if flight_over_no==0:
                            flight_city=f" {cityTo}-{cityCodeTo}"
                        elif flight_over_no>0:
                            flight_city+=f" {cityTo}-{cityCodeTo} "
                        cityCodeTo=temp['data'][0]['cityCodeTo']
                        break
                
                    
                elif temp['data'][0]['route'][flight_over_no]['cityCodeTo']!=iata_city:
                        if  flight_over_no==0:
                            flight_city+=f" {cityTo}-{cityCodeTo}"
                        else:
                            flight_city+=f" Then {cityTo}-{cityCodeTo}"
                        flight_over_no+=1
                        print(flight_over_no)
            emails=[]
            for i in data.send_email_data():
                emails.append(i['email'])
                
            notify.send_sms(price,cityFrom,cityCodeFrom,cityTo,cityCodeTo,out_date,return_date,flight_over_no,flight_city)
            notify.send_mail(price,cityFrom,cityCodeFrom,cityTo,cityCodeTo,out_date,return_date,flight_over_no,flight_city,emails)

        except(IndexError):
            print(f"No flights found for {iata_city}.")
            return None
        
    #This class is responsible for talking to the Flight Search API.