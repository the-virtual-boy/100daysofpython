from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import dotenv_values

config = dotenv_values("../.env")

KEY = config['TMDB_KEY']
TOKEN = config['API_TOKEN']
URL = f"https://api.themoviedb.org/3/search/movie?api_key={KEY}&"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
Bootstrap5(app)

class ReviewForm(FlaskForm):
    rating = StringField('Your Rating Out of 10')
    review = StringField(label='Your Review')
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

## to pre-populate the DB with movies
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movie_list = result.scalars().all()[::-1]
    for movie in movie_list:
        movie.ranking = movie_list.index(movie) + 1
    return render_template("index.html", movies = movie_list)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = ReviewForm()
    movie_id = request.args.get('id', 0, type=int)
    result = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
    # form.rating.data = result.rating
    # form.review.data = result.review
    if request.method == "POST":
        if form.validate_on_submit:
            if not form.rating.data and not form.review.data:
                return home()
            if form.rating.data:
                new_rating = form.rating.data
                result.rating = new_rating
            if form.review.data:
                new_review = form.review.data
                result.review = new_review
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return render_template("edit.html", movie=result, form=form)
    
@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id', 0, type=int)
    result = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if request.method == "POST":
        if form.validate_on_submit:
            title = form.title.data
            response = requests.get(f'{URL}query={title}')
            # print(response.json()['results'][0]['title'])
            movie_list = response.json()['results']
            return render_template("select.html", movies=movie_list)
    else:
        return render_template("add.html", form=form)

@app.route("/db_add")
def db_add():
    movie = request.args.get('new_movie', type=dict)
    new_movie = Movie(
        id = request.args.get('id', type=int),
        title = request.args.get('title'),
        year = request.args.get('date', type=int),
        description = request.args.get('description'),
        img_url = f"https://image.tmdb.org/t/p/w500/{request.args.get('img_url')}"
    )

    db.session.add(new_movie)
    db.session.commit()
    print(new_movie.id)

    return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
