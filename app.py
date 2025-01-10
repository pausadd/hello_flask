# https://code.visualstudio.com/docs/python/tutorial-flask
import re
from datetime import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    fichero="hello_there.html"
    return render_template(
        fichero,
        name=name,
        date=datetime.now()
    )

# 
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
        
# "C:\Users\Pablo\OneDrive\Pictures\foto Pim Pum Salamanca.jpg"