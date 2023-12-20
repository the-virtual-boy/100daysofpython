from flask import Flask, render_template, request
import requests
from dotenv import dotenv_values
import smtplib


config = dotenv_values(".env")

EMAIL = config["EMAIL_ADDRESS"]
PASSWORD = config["EMAIL_PASSWORD"]
TO_ADDR = config["TO_ADDRESS"]
SMTP = "smtp.gmail.com"


# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c803554640b9496d3bcd").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=request.form["email"],
                to_addrs=TO_ADDR,
                msg=f"Subject:Blog Message Submitted!\n\nName: {request.form['name']}\nEmail: {request.form['email']}\n"
                    f"Phone: {request.form['phone']}\nMessage: {request.form['message']}!"
            )
        return render_template("contact.html", submit=True )
    else:
        return render_template("contact.html", submit=False )


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True, port=5001)


