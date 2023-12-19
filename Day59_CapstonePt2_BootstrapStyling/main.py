from flask import Flask, render_template
import requests
import datetime

URL = "https://api.npoint.io/c803554640b9496d3bcd"

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get(URL).json()
    date = datetime.datetime.now()
    return render_template('index.html', posts=data, date=date.strftime('%B %d, %Y') )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    post = next(blog for blog in all_posts if blog["id"] == int(num))
    data = requests.get(URL).json()
    date = datetime.datetime.now()
    return render_template("post.html", post=post, date=date.strftime('%B %d, %Y'))

if __name__ == '__main__':
    app.run(debug=True)