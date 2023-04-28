import requests
from datetime import datetime

ID = "b0d7b587"
KEY = "a83921893402f60e8df378cb01ac5f27"

nutritionix_api_endpoits = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_header = {
    "x-app-id": ID,
    "x-app-key": KEY
}

nutritionix_config = {
    "query": input("type here:-"),
    "gender": "male",
    "weight_kg": "48",
    "height_cm": "182.88",
    "age": "18"
}


sheety_api_endponit = "https://api.sheety.co/9e60f5f232706ee5e9eab5b103f92f40/workout/workouts"

today = datetime.now()
response = requests.post(url=nutritionix_api_endpoits,
                         headers=nutritionix_header, json=nutritionix_config).json()


sheety_config = {
    "workout":{
        "date": today.date().strftime("%B %d, %Y"),
        "time": today.time().strftime("%I %M %p"),
        "exercise": response["exercises"][0]['name'],
        "duration": response["exercises"][0]['duration_min'],
        "calories": response["exercises"][0]['nf_calories']
    }
}
sheety_header={"Authorization":"Basic a2FzaGlmOkFxdWF0eXBlMTIh"}

print(sheety_config)
response_sheety = requests.post(url=sheety_api_endponit, json=sheety_config,headers=sheety_header)
print(response_sheety.text)
