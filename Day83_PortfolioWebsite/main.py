from datetime import date
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from forms import ContactForm, RegisterForm, LoginForm
from dotenv import dotenv_values

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(current_user.get_id())
        print(type(current_user.get_id()))
        if not current_user.is_authenticated or current_user.get_id() != "1":
            print("not allowed!")
            return redirect(url_for('login'))
            # abort(403)
        return f(*args, **kwargs)
    return decorated_function

config = dotenv_values('../.env')
KEY = config['SECRET_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy()
db.init_app(app)

@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Message(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    date = db.Column(db.String(250), nullable=False)

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
            message=form.message.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(message)
        db.session.commit()
        flash("Your message has been sent!", "success")
        return redirect("/")
    return render_template('index.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
                email=request.form.get("email"), 
                password=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8), 
                name=request.form.get("name")
            )
        if db.session.execute(db.select(User).where(User.email == user.email)).scalar():
            flash('Account already exist!\nPlease Login.')
            return redirect(url_for('login'))
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Succesfully registered!')
        return redirect(url_for("admin"))
    return render_template("register.html", registration_form=form )

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result:
            user = result
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('admin'))
            else:
                flash('Incorrect password')
                return redirect(url_for('login'))
        else:
            flash('no such user')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)

@app.route('/admin', methods=['POST', 'GET'])
@admin_only
def admin():
    messages = Message.query.order_by(Message.date.desc()).all()
    return render_template('admin.html', messages=messages)

@app.route('/admin/<int:message_id>', methods=['POST', 'GET'])
@admin_only
def delete_message(message_id):
    message_to_delete = db.get_or_404(Message, message_id)
    db.session.delete(message_to_delete)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)