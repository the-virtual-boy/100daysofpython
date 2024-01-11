from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from forms import ContactForm
from dotenv import dotenv_values

config = dotenv_values('../.env')
KEY = config['FLASK_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy()
db.init_app(app)

class Message(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    message = db.Column(db.String(1000))

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(
            email=form.email.data,
            name=form.name.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash("Your message has been sent!", "success")
        return redirect("/")
    return render_template('index.html', form=form)





if __name__ == "__main__":
    app.run(debug=True, port=5000)