# Con la refactorizacion este fichero no vale para nada
# https://code.visualstudio.com/docs/python/tutorial-flask
import re
from datetime import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)


# Replace the existing home function with the one below   
"""    
@app.route("/")
def home():
    return "Hello, Flask!"
"""

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")



@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

# serve static file in code
# usado para api's
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
        
# "C:\Users\Pablo\OneDrive\Pictures\foto Pim Pum Salamanca.jpg"