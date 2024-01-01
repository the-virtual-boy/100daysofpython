from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from sqlalchemy import update

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class Blog_Form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField("Sub-Title", validators=[DataRequired()])
    author = StringField("Author")
    img_url = StringField("Image URL", validators=[URL(), DataRequired()])
    body = CKEditorField("Body", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

# TODO: add_new_post() to create a new blog post
@app.route("/add-new-post", methods=["GET", "POST"])
def add_new_post():
    form = Blog_Form()
    if request.method == "POST":
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data,
            date = date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=form)    

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<id>", methods=["GET", "POST"])
def edit_post(id):
    post = db.session.query(BlogPost).filter_by(id=id).scalar()     
    form = Blog_Form(title=post.title, subtitle=post.subtitle, body=post.body, 
                     author=post.author, img_url=post.img_url)
    if request.method == 'POST':
        # update the record with the new info
        data = { f'{field.id}': f'{field.data}' for field in form if field.id in 
                ['title', 'subtitle', 'body', 'author', 'img_url']}
        db.session.query(BlogPost).filter_by(id=id).update(data)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    else:        
        return render_template('make-post.html', form=form)    

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):  
    post = db.session.query(BlogPost).filter_by(id=post_id).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5003)
