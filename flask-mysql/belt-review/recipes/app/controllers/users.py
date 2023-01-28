from app import app
from flask_bcrypt import Bcrypt
from app.models.user import User
from flask import render_template, redirect, request, session, flash

@app.route('/')
def index():
    return render_template("index.html")