from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://instagram.com"


def safe_click(element):
    while True:
        try:
            element.click()
            sleep(1)
            return
        except:
            pass


class InstaFollower:
    def __init__(self, user, pw):
        self.url = URL
        self.user = user
        self.pw = pw

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(self.url)
        sleep(1)
        user_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        safe_click(user_box)
        user_box.send_keys(self.user)

        pw_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        safe_click(pw_box)
        pw_box.send_keys(self.pw + Keys.ENTER)
        sleep(4)
        while True:
            try:
                no_save_creds = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
                safe_click(no_save_creds)
            except:
                sleep(.1)
            else:
                break
        sleep(2)
        while True:
            try:
                no_notif = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                safe_click(no_notif)
            except:
                sleep(.1)
            else:
                return

    def search(self, target):
        while True:
            try:
                search_button = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div')
            except:
                print("no search")
                sleep(1)
            else:
                safe_click(search_button)
                break

        self.driver.switch_to.active_element.send_keys(target + Keys.ENTER)
        sleep(1)
        account = self.driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
        sleep(1)
        safe_click(account)
        sleep(3)

    def follow(self):
        follower_link = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        safe_click(follower_link)
        sleep(2)
        followers = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        print(followers)
        follower_buttons = followers.find_elements(By.XPATH, '//*[text()="Follow"]')
        print(follower_buttons)

        for button in follower_buttons:
            print(button)
            safe_click(button)
