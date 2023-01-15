from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

# @app.route('/')
# def home():
#     redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojo.html")