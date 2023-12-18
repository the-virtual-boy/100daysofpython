import random
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

URL1 = "https://api.agify.io/?name="
URL2 = "https://api.genderize.io?name="

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now()
    return render_template("index.html", num=random_number, year=str(year.strftime('%Y')))

@app.route('/guess/')
def guess():
    return "Give me a name in the URL!"

@app.route('/guess/<name>')
def guess_info(name):
    
    age = requests.get(URL1 + name).json()

    gender = requests.get(URL2 + name).json()

    return render_template("guess.html", name=name, gender=gender['gender'], age=str(age['age']))

@app.route('/blog/<num>')
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    print(num)
    return render_template("blog.html", blogs=all_posts)
    


if __name__ == "__main__":
    app.run(debug=True)


