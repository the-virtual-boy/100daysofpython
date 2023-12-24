from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('lesson.html')

@app.route('/login', methods=['POST'])
def receive_data():
    return f'<h1>username = {request.form["name"]}, password = {request.form["password"]}'

if __name__ == '__main__':
    app.run(debug=True)