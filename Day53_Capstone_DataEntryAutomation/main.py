from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values("../.env")

FORMS_LINK = config['GOOGLE_FORMS_LINK']
URL = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

request = requests.get(URL)
page = request.text

soup = BeautifulSoup(page, "lxml")

search = soup.find_all("li", class_='ListItem-c11n-8-84-3-StyledListCardWrapper')


homes = [{'link': item.find("a").get("href"), 'address': ','.join(item.find("address").get_text().split(',')[-3:]).split('|')[-1].strip(), 'price': item.find("span", class_="PropertyCardWrapper__StyledPriceLine").get_text()[0:6]} for item in search ]

driver.get(FORMS_LINK)

sleep(2)



for home in homes:
    inputs = [
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"),
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"),
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"),
    ]

    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    sleep(2)
    inputs[0].send_keys(home['link'])
    inputs[1].send_keys(home['address'])
    inputs[2].send_keys(home['price'])
    submit_button.click()
    sleep(2)
    again_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    again_button.click()
    sleep(3)