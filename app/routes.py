from flask import render_template
from app import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required

"""Main Routes"""
@app.route("/")
def home():
    return render_template("index.html")