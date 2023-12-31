from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import randint

KEY = "TopSecretAPIKey"
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random():
    cafe = db.session.execute(db.select(Cafe).order_by(db.func.random())).scalars().first()
    print(cafe.name)
    return jsonify(cafe=cafe.as_dict())
        ## Self formatted jsonify, switched to whole table
        #            {
        # "can_take_calls": cafe.can_take_calls, 
        # "coffee_price": cafe.coffee_price, 
        # "has_sockets": cafe.has_sockets, 
        # "has_toilet": cafe.has_toilet,
        # "has_wifi": cafe.has_wifi,
        # "id": cafe.id,
        # "img_url": cafe.img_url,
        # "location": cafe.location,
        # "map_url": cafe.map_url,                    
        # "name": cafe.name, 
        # "seats": cafe.seats,
        # })

@app.route("/all")
def get_all():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.as_dict() for cafe in cafes])


@app.route("/search")
def find_cafe():
    loc = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).filter_by(location=loc)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.as_dict() for cafe in cafes])
    else:
        return jsonify({"error": 
                        {
                            "Not Found": "Sorry, no cafes at that location"
                        }})


# HTTP POST - Create Record
    
@app.route("/add", methods=['POST'])
def add_cafe():
    print(request.form.get('name'))
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url =  request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response = {
            "success": f"Succesfully added {new_cafe.name}."
        }
    )
    

# HTTP PUT/PATCH - Update Record

@app.route("/update-price", methods=['PATCH'])
def update_price():
    id = int(request.args.get("id"))
    new_price = request.form.get('coffee_price')
    cafe = db.get_or_404(Cafe, id, description="No such ID exists in database")
    print(id, new_price, cafe.coffee_price)
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"Success":"Price updated!"}), 200


# HTTP DELETE - Delete Record

@app.route("/report-closed/<id>", methods=['DELETE'])
def delete_cafe(id):
    print(id)
    key = request.args.get("api-key")
    if key == KEY:
        cafe = db.get_or_404(Cafe, id)
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"message":f"{cafe.name} deleted"}), 200
    else:
        return jsonify(response={"error":"Incorrect API Key!"}), 403


if __name__ == '__main__':
    app.run(debug=True)
