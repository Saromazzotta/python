from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

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
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/ninja/add', methods=['POST'])
def add_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }

    Ninja.save(data)
    return redirect(f'/dojos/{user_id}')

# @app.route('/ninja/<int:dojo_id>/update')
# def update_ninja():
#     pass

# @app.route('/ninja/<int:dojo_id/delete')
# def delete_ninja():
#     pass
