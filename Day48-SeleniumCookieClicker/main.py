import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://orteil.dashnet.org/experiments/cookie/"
SHOP_TIME = 3
TIMEOUT = 299
OUTPUT = {
    'Time machine': 123456,
    'Portal': 6666,
    'Alchemy lab': 500,
    'Shipment': 100,
    'Mine': 50,
    'Factory': 20,
    'Grandma': 4,
    'Cursor': 1,
}


def shopTimerTrigger(turn, to_buy=''):
    global buy, nb
    cookies = driver.find_element(By.ID, "money").text.replace(',', '')
    shop = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    items = [{"name": i.text.split("-")[0].strip(), "cost": int(i.text.split("-")[1].strip().replace(',', ''))} for i in
             shop if i.text != ""]

    to_buy, efficiency = calculate_efficiency(items[::-1], cookies)

    set_grandma_upgrade(to_buy)
    print(to_buy, efficiency, .025 * 1 / ((turn // 20) + .9) )
    if is_efficient(efficiency, turn):
        print('buy')
        buy += 1
        time.sleep(.1)
        purchase = driver.find_element(By.ID, f"buy{to_buy}")
        purchase.click()
    else:
        print("no buy")
        nb += 1

def set_grandma_upgrade(to_buy):
    if OUTPUT['Grandma'] < 5 and to_buy == 'Factory':
        OUTPUT['Grandma'] = 5
    elif OUTPUT['Grandma'] < 7 and to_buy == 'Mine':
        OUTPUT['Grandma'] = 7
    elif OUTPUT['Grandma'] < 10 and to_buy == 'Shipment':
        OUTPUT['Grandma'] = 10
    elif OUTPUT['Grandma'] < 14 and to_buy == 'Alchemy lab':
        OUTPUT['Grandma'] = 14


def calculate_efficiency(items, cookies, efficiency=-1, index=0, to_buy = 'Time machine'):
    if index in range(0, len(items)):
        print(index, items[index])
        i = items[index]
        print('-', i)
        if int(i['cost']) * 3/4 < int(cookies) and OUTPUT[i['name']] / i['cost'] > efficiency:
            efficiency = OUTPUT[i['name']] / i['cost']
            to_buy = i['name']
            print('----', to_buy, efficiency)

        to_buy, efficiency = calculate_efficiency(items, cookies, efficiency, index + 1, to_buy)
    return to_buy, efficiency

def is_efficient(efficiency, turn):
    return efficiency > .025 * 1 / ((turn // 15) + .7)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
buy = 0
nb = 0
turn = 1
time_Start = time.time()
while time.time() < time_Start + TIMEOUT:
    cookie.click()
    if time.time() >= time_Start + (SHOP_TIME * turn):
        shopTimerTrigger(turn)
        turn += 1
shopTimerTrigger(100)
cps = driver.find_element(By.ID, "cps")
print("final score: ", cps.text.split(' ')[2], "buy:", buy, "no buy:", nb)
