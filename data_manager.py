import requests
from pprint import pprint

URL = 'https://api.sheety.co/1c296835569c77d1fcd715ee9a2f3d13/filghtDealsProject/prices'
PUTURL = 'https://api.sheety.co/1c296835569c77d1fcd715ee9a2f3d13/filghtDealsProject/prices/'



class DataManager:
    def __init__(self):
        self.sheet_data = self.get_data()

    def get_data(self):
        response = requests.get(url=URL)
        data = response.json()['prices']
        return data

    def put_data(self, payload):
        url = f"{PUTURL}{payload["price"]['id']}"
        response = requests.put(url=url, json=payload)

