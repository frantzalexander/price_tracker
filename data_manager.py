import requests
from decouple import config

class DataManager:
    def __init__(self):
        self.__user_agent = config("USER_AGENT")
        self.__accept_language = config("ACCEPT_LANGUAGE")
        self.__accept = config("ACCEPT")
        self.__accept_encoding = config("ACCEPT_ENCODING")
        self.__dnt = config("DNT")
        self.headers = {
            "User-Agent": self.__user_agent,
            "Accept": self.__accept,
            "Accept-Language": self.__accept_language,
            "Accept_Encoding": self.__accept_encoding,
            "dnt": self.__dnt
        }
    
    def get_website_data(self, website_url):
        self.website_url = website_url
        self.website_data = requests.get(
            url = self.website_url,
            headers =self.headers 
            )
        self.website_data_text = self.website_data.text
        return self.website_data_text
     