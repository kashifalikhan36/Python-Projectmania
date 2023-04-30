import requests
from pprint import pprint
SHEETY_API_ENDPOINTS="https://api.sheety.co/f9dd6f5b40aeef7d9f6f6a1cc5b520a3/flightDeals/prices"
sheety_header={"Authorization":"Basic a2FzaGlmOkFxdWF0eXBlMQ=="}
response_sheety = requests.get(url=SHEETY_API_ENDPOINTS,headers=sheety_header)
pprint(response_sheety.json())