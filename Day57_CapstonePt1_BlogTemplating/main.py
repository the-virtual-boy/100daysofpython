from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("index.html", blogs=all_posts)

@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    post = next(blog for blog in all_posts if blog["id"] == int(num))
    print(post)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
