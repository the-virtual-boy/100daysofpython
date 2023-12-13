import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
from plyer import notification
from time import sleep 

config = dotenv_values("../.env")

EMAIL = config["LINKEDIN_USER"]
PASS = config["LINKEDIN_PASS"]
URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3780622310&distance=25&f_AL=true&f_E=4&f_WT=2%2C3&geoId"
       "=105142029&keywords=devops%20engineer&location=&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true"
       "&sortBy=R")


def elements_exists(value):
    try:
        driver.find_element(By.XPATH, value)
        return True
    except Exception:
        return False

def safe_click(object):
    while True:
        try:
            object.click()
            sleep(1)
            return
        except:
            pass


def apply_to_job():
    ez_apply = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
    safe_click(ez_apply)
    while elements_exists('//*[@id="jobs-apply-header"]'):
        sleep(1)
        next_button = driver.find_element(By.XPATH, '//span[text()="Next"] | //span[text()="Review"] | //span[text('
                                                    ')="Submit application"]')

        if next_button.text == "Submit application":
            safe_click(next_button)
            exit_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Dismiss"]')
            exit_button.click()
            sleep(1)
        else:
            safe_click(next_button)

            if elements_exists('//*[contains(@role, "alert")]'):
                notification.notify(
                    title="User Input Needed",
                    message="Ran into questions that require user input!",
                    app_icon=None,
                    timeout=10,
                )
                ask = input("Should we continue with this application?: ")
                if ask[0] != 'y':
                    exit_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Dismiss"]')
                    safe_click(exit_button)
                    discard_button = driver.find_element(By.XPATH, '//span[text()="Discard"]')
                    safe_click(discard_button)
                    return
                sleep(.1)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

login_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_button.click()

user_box = driver.find_element(By.XPATH, '//*[@id="username"]')
user_box.click()
user_box.send_keys(EMAIL)

pass_box = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_box.click()
pass_box.send_keys(PASS + Keys.ENTER)

input("because of bot defense")

page = 1
while True:
    if elements_exists("//button[contains(@class, 'jobs-apply-button')]"):
        apply_to_job()
    results = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
    for result in results:
        safe_click(result)
        print(result.text)
        print("")
        if elements_exists("//button[contains(@class, 'jobs-apply-button')]"):
            sleep(.1)
            apply_to_job()

    notification.notify(
        title="Finished",
        message="One pass through finished",
        app_icon=None,
        timeout=10,
    )
    ask = input("All originally loaded scripts finished, see if there's any new loaded positions and continue?: ")
    if ask[0] != 'y':
        break
    else:
        page += 1
        print(page)
        search = f"//button[@aria-label='Page {str(page)}']"
        if elements_exists(search):
            next_page = driver.find_element(By.XPATH, f'//button[@aria-label="Page {str(page)}"]')
            safe_click(next_page)
            sleep(2)
