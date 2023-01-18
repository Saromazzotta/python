from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos=dojos)

@app.route('/dojos/new/', methods=['POST'])
def add_dojo():
    data = {
        "name" : request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def ninja_show(dojo_id):
    data = {
        "id" : dojo_id
    }
    return render_template("show.html", dojo=Dojo.get_dojo_with_ninjas(data))

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")
