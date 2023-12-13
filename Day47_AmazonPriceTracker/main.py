from pprint import pprint

import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values
import smtplib


config = dotenv_values("../.env")

EMAIL = config["EMAIL_ADDRESS"]
PASSWORD = config["EMAIL_PASSWORD"]
TO_ADDR = config["TO_ADDRESS"]
URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"
PRICE_LIMIT = 105.00
SMTP = "smtp.gmail.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7",
}

request = requests.get(URL, headers=headers)
page = request.text

soup = BeautifulSoup(page, "lxml")

dollars = soup.find("span", class_="a-price-whole").get_text()
cents = soup.find("span", class_="a-price-fraction").get_text()
price = float(dollars) + float(cents) / 100

if price < PRICE_LIMIT:
    print("Deal!")
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_ADDR,
            msg=f"Subject:Price Drop!\n\nPrice is currently {price}, which is {PRICE_LIMIT - price} dollars less "
                f"than your limit of {PRICE_LIMIT}!"
        )

# pprint(soup.find("span", id="productTitle").get_text())