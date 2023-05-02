from data_manager import DataManager
from flight_search import FlightSearch

flight_search=FlightSearch()
class FlightData:
    def __init__(self):
        self.minimum_price=[]
        # self.price=0
        self.iata=''
        self.all_data=DataManager().all_data()
        rec=2
        for i in self.all_data:
            self.data=DataManager().give(rec)
            rec+=1
            self.minimum_price.append(self.data['lowest'])
            # if self.price<self.data['lowest']:
            #     self.price=self.data['lowest']
        for i in self.all_data:
            if i['lowest']==min(self.minimum_price):
                self.iata=i['iata']
        flight_search.flight_final_data_search(self.iata)    
            

    #This class is responsible for structuring the flight data.