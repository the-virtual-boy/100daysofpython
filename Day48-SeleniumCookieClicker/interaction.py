from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# count = driver.find_element(By.LINK_TEXT, "All portals")
# count.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python" + Keys.ENTER)

# fn_box = driver.find_element(By.NAME, "fName")
# ln_box = driver.find_element(By.NAME, "lName")
# em_box = driver.find_element(By.NAME, "email")
#
# fn_box.click()
# fn_box.send_keys("Bob")
# ln_box.click()
# ln_box.send_keys("Bobby")
# em_box.click()
# em_box.send_keys("Bob.Bobby@bobbers.com" + Keys.ENTER)

# driver.quit()