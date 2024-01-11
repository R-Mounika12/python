from flask import Flask

# creating a Flask app instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to Flask app"

app.run('0.0.0.0')