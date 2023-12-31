from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
# This is called by Flask-Login to retrieve the current logged in user
# You can replace this with any database call (e.g., using SQLAlchemy)
    return db.get_or_404(User, id)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html', logged_in=current_user.is_authenticated)
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
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
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email=request.form.get("email"), 
        password=request.form.get("password")
        print(email)
        print(email[0])
        result = db.session.execute(db.select(User).where(User.email == email[0])).scalar()
        if result:
            user = result
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Incorrect password')
                return render_template('login.html')
        else:
            flash('no such user')
            return render_template('login.html')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():    
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
