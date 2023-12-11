import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://orteil.dashnet.org/experiments/cookie/"
SHOP_TIME = 5
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

timeout = 300

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# part of new cookie clicker
# while True:
#     try:
#         driver.find_element(By.ID, "langSelect-EN")
#     except:
#         time.sleep(2)
#     else:
#         english = driver.find_element(By.ID, "langSelect-EN")
#         break
# english.click()
# time.sleep(5)
# cookie = driver.find_element(By.ID, "bigCookie")

cookie = driver.find_element(By.ID, "cookie")
cookies = driver.find_element(By.ID, "money")
shop = driver.find_elements(By.CSS_SELECTOR, "#store div b")

# for i in shop:
#     if i.text != "":
#         name, cost = i.text.split("-")
#         items.append({'name': name, 'cost': cost})

# items = [{"name": i.text.split("-")[0].strip(), "cost": i.text.split("-")[1].strip().replace(',','')} for i in shop if i.text != ""]
# print(items)

time_Start = time.time()
tobuy = ""
turn = 1
while time.time() < time_Start + timeout:
    efficiency = -1
    cookie.click()
    # print(time.time() - time_Start)
    if time.time() >= time_Start + (SHOP_TIME * turn):
        turn += 1
        cookies = driver.find_element(By.ID, "money").text.replace(',', '')
        shop = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        items = [{"name": i.text.split("-")[0].strip(), "cost": int(i.text.split("-")[1].strip().replace(',', ''))} for i in
                 shop if i.text != ""]
        for i in items[::-1]:
            print('-', i)
            if int(i['cost']) < int(cookies) and OUTPUT[i['name']] / i['cost'] > efficiency:
                efficiency = OUTPUT[i['name']] / i['cost']
                tobuy = i['name']
                print('----', tobuy, efficiency)
        if OUTPUT['Grandma'] < 5 and tobuy == 'Factory':
            OUTPUT['Grandma'] = 5
        elif OUTPUT['Grandma'] < 7 and tobuy == 'Mine':
            OUTPUT['Grandma'] = 7
        elif OUTPUT['Grandma'] < 10 and tobuy == 'Shipment':
            OUTPUT['Grandma'] = 10
        elif OUTPUT['Grandma'] < 14 and tobuy == 'Alchemy lab':
            OUTPUT['Grandma'] = 14
        if(efficiency > .025 * 1 / ((turn // 20) + .9)):
            time.sleep(.1)
            purchase = driver.find_element(By.ID, f"buy{tobuy}")
            purchase.click()
cps = driver.find_element(By.ID, "cps")
print("final score: ", cps.text.split(' ')[2])