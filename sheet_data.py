import requests
from decouple import config

class SpreadsheetData:
    def __init__(self):
        self.sheet_data: str = config("SHEET_URL")
        self.__sheet_api_key: str = config("TOKEN")
        self.__headers = {
            "Authorization": self.__sheet_api_key
        }
    
    def get_product_data(self):
        self.response = requests.get(
            url = self.sheet_data,
            headers = self.__headers
        )
        self.response.raise_for_status()
        
        return self.response.json()