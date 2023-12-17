from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>" 
    return wrapper    

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>text</p>:" \
        "<img src='https://maryfrancesflood.com/wp-content/uploads/2016/02/the-whole-is-greater-than-the-sum-of-its-parts.jpg' width=3000>"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye'

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you're number {number}!"


if __name__ == "__main__":
    app.run(debug=True)






## ********Day 55 Start**********

## Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)