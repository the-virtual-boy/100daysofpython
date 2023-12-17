import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3kwN3M0YTBiM2hhN29wZjkxbndqMnM5ZmptcHczMGdzZzJkM2VkbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tXL4FHPSnVJ0A/giphy.gif'>"

@app.route("/<int:num>")
def guess(num):
    if num == to_guess:
        return "<h1>Congratulations, you got it!</h1>" \
               "<image src='https://media0.giphy.com/media/yJFeycRK2DB4c/200.webp?cid=ecf05e47e6uv0hy036uxrg3zy1ljbj2hr6hj3w5q4ok5koq2&ep=v1_gifs_search&rid=200.webp&ct=g'>"
    elif num < to_guess:
        return "<h1>Too low!</h1>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG5qY2llNjVzaGgzeWJiNW9kb3dhamJlcnUwZm5ocHpkdDFlZzg3YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PUyaulKbPUCt9Weht9/giphy.gif'>"
    else:
        return "<h1>Too High</h1>" \
               "<img src='https://media0.giphy.com/media/t9l9L8qFKJfsFn2WLm/giphy.gif?cid=ecf05e477rtq53hbykdfd872jctzgom5kp7c54ihn096lea2&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"


to_guess = random.randint(0,9)

if __name__ == "__main__":
    app.run(debug=True)

