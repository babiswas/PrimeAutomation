from flask import render_template
from Route.route import home

@home.route('/')
def home():
    return render_template("home.html")






