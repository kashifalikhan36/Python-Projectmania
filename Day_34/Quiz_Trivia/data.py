import requests
import json
response=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()
question_data = response['results']