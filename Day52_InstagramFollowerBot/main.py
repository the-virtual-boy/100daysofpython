from InstaFollower import InstaFollower
from dotenv import dotenv_values

config = dotenv_values("../.env")

USER = config['INSTAGRAM_USERNAME']
PASS = config['INSTAGRAM_PASSWORD']
TARGET_ACCOUNT = "chefsteps"

bot = InstaFollower(USER, PASS)

bot.login()
bot.search(TARGET_ACCOUNT)
bot.follow()
