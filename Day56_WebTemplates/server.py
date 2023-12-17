from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('angela.html')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



## make any page editable in chrome:

# inspect > console
    # document.body.contentEditable=true