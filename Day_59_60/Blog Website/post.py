import requests
class Post:
    def __init__(self):
        self.response=requests.get(url='https://api.npoint.io/5b86cb1c2278d8471563').json()
    
    def post(self):
        return self.response