from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = results.scalars()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
     if request.method == 'POST':
         with app.app_context():
            book = Book()
            book.title = request.form['name']
            book.author = request.form['author']
            book.rating = request.form['rating']
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
     return render_template('add.html')

@app.route("/edit",  methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        rating = float(request.form['rating'])
        print(rating)
        book_id = request.args.get('id', 0, type=int)
        print(id)
        result = db.session.execute(db.select(Book).filter_by(id=id)).scalar_one()
        print(result)
        result.rating = rating
        db.session.commit()
        return home()
    else:
        book_id = request.args.get('id', 0, type=int)
        print(book_id)
        result = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
        print(result)
        return render_template("edit.html", book=result)
    
@app.route("/delete")
def delete():
    book_id = request.args.get('id', 0, type=int)
    result = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
    # result = db.get_or_404(Book, book_id)
    print(result)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

