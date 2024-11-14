import smtplib

from decouple import config

class Notifier:
    def __init__(self):
        self.__receiver = config("RECEIVER_EMAIL")
        self.__sender = config("SENDER_EMAIL")
        self.__app = config("APP_PASSWORD")
        self.__smtp = config("SMTP_ADDRESS")
        
    def send_email(self, product_name: str, product_price: float, message: str):
        self.product_name = product_name
        self.message = message
        self.product_price = product_price
        with smtplib.SMTP(self.__smtp, port= 587) as connection:
            connection.starttls()
            connection.login(
                user = self.__sender,
                password = self.__app
            )
            connection.sendmail(
                from_addr = self.__sender,
                to_addrs= self.__receiver,
                msg = f"Subject: The {self.product_name} price has decreased on Amazon to ${self.product_price}. \n\n {self.message}."
            )