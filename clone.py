import requests
from bs4 import BeautifulSoup
from notification import Notifier
from decouple import config


notifier = Notifier()

website_url = config("STATIC_WEBSITE_URL")

response = requests.get(
    url = website_url
)

response.raise_for_status()

website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

price_dollars_text = soup.find(
    name = "span",
    class_ = "a-price-whole"
).getText()

price_dollars = int(price_dollars_text.split(".")[0])

price_cents_text = soup.find(
    name = "span",
    class_ = "a-price-fraction"
).getText()

price_cents = float(price_cents_text) / 100

product_price = price_dollars + price_cents

product = "Pressure Cooker"
target_price = 100
message = f"The {product} link: {website_url}"

if product_price < target_price:
    notifier.send_email(
        product_name = product, 
        product_price = product_price, 
        message = message
        )