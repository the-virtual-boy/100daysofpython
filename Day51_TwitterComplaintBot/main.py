from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

config = dotenv_values("../.env")

USER = config["TWITTER_USERNAME"]
PASS = config["TWITTER_PASSWORD"]
URL = "https://www.speedtest.net/"
UP = 10
DOWN = 400

bot = InternetSpeedTwitterBot(URL, DOWN, UP, USER, PASS)

speed = bot.get_internet_speed()
if bot.speed_is_low():
    bot.tweet_at_provider()

# bot.tweet_at_provider()