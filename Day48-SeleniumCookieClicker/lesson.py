from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.python.org"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents= driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollars.text}.{price_cents.text}")

# search = driver.find_element(By.NAME, value="q")
# print(search.tag_name)
# print(search.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc.text)
# time.sleep(10)

# bug_link =driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.find_elements(By.CSS_SELECTOR, value="")
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = [{'time': i.text,'name': j.text} for (i, j) in zip(event_times,event_names)]
final_events = {events.index(i): i for i in events}


print(final_events)

driver.quit()