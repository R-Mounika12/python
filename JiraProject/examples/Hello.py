from flask import flask

# creating a Flask app instance
app = Flask(_name_)

@app.route('/')
def hello-world():
    return "Welcome to Flask app"

app.run('0.0.0.0')
