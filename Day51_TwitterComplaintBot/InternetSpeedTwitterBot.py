from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def safe_click(element):
    while True:
        try:
            element.click()
            sleep(1)
            return
        except:
            pass


class InternetSpeedTwitterBot:
    def __init__(self, url, down, up, user, pw):
        self.url = url
        self.user = user
        self.pw = pw
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down_limit = down
        self.up_limit = up

    def get_internet_speed(self):
        self.driver.get(self.url)
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '1]/a/span[4]')
        safe_click(button)

        while True:
            try:
                down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                          '2]/span')
                up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                        '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                        '2]/span')
                if up.text == '' or up.text == '—':
                    sleep(.1)
                else:
                    break
            except:
                sleep(.1)
        self.speed = {'up': float(up.text), 'down': float(down.text)}
        return self.speed
    def tweet_at_provider(self):
        print("tweeting spectrum!")
        twitter = self.driver.get("https://twitter.com/home")
        sleep(1)
        user_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                        '2]/div/input')
        safe_click(user_input)
        user_input.send_keys(self.user + Keys.ENTER)
        sleep(1)
        pw_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                      '3]/div/label/div/div[2]/div[1]/input')
        safe_click(pw_input)
        pw_input.send_keys(self.pw + Keys.ENTER)
        sleep(3)
        draft_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                       '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                       '1]/div/div/div/div/div/div[2]/div/div/div/div')
        safe_click(draft_box)
        message = (f"Why is my up/down {self.speed['down']}/{self.speed['up']} when I'm paying for {self.down_limit}/"
                   f"{self.up_limit}?")
        draft_box.send_keys(message + Keys.ENTER)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                                  '2]/div/div/div/div[3]/div/span/span')
        safe_click(post)


    def speed_is_low(self):
        print(self.speed['up'], self.up_limit, self.speed['down'], self.down_limit)
        if self.speed['up'] < self.up_limit or self.speed['down'] < self.down_limit:
            return True
        else:
            return False

