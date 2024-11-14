from bs4 import BeautifulSoup

from pprint import PrettyPrinter
from sheet_data import SpreadsheetData
from data_manager import DataManager
from notification import Notifier

pp= PrettyPrinter(indent = 2)

data = SpreadsheetData()
website_text_data = DataManager()
notify = Notifier()

product_data = data.get_product_data()

product_name_list = []
product_url_list = []
target_price_list = []
website_data = []

for product in product_data["sheet1"]:
    product_url = product["productUrl"]
    product_name_list.append(product["product"])
    product_url_list.append(product_url)
    target_price_list.append(product["priceDiscount"])
    website_data.append(website_text_data.get_website_data(product_url))
    print(product["productUrl"])
    
index = 0
current_product_price_list = []
for website in website_data:
    soup = BeautifulSoup(website, "html.parser")
    price_dollars_text = soup.find(
        name = "span",
        class_ = "a-price-whole"
        ).getText()
    price_dollars_unformatted = price_dollars_text.split(".")[0]
    if len(price_dollars_unformatted) > 3:
        price_dollars_thousands, price_dollars_hundreds = price_dollars_unformatted.split(",")
        price_dollars_formatted = int(price_dollars_thousands + price_dollars_hundreds)
    
    else:
        price_dollars_formatted = int(price_dollars_unformatted)
        
    price_cents_text = soup.find(
        name = "span",
        class_ = "a-price-fraction"
        ).getText()
    
    price_cents = float(price_cents_text) / 100
    current_product_price: float = price_dollars_formatted + price_cents
    current_product_price_list.append(current_product_price)
    
for price in current_product_price_list:
    
    if price <= target_price_list[index]: 
        send_product_name = product_name_list[index]
        send_product_url = product_url_list[index]
        email_message = f"The {send_product_name} link: {send_product_url}"
        
        notify.send_email(
            product_name = send_product_name,
            product_price = price,
            message = email_message
        )
        
    index += 1