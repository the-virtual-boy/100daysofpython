import sqlite3, flask, flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-book-collection.db"
db.init_app(app)

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.FLOAT, nullable=False)

with app.app_context():
    db.create_all()

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
    

with app.app_context():
    book = Books()
    book.id = 1
    book.title = 'Harry Potter'
    book.author = 'J. K. Rowling'
    book.rating = 9.3
    db.session.add(book)
    db.session.commit()

    