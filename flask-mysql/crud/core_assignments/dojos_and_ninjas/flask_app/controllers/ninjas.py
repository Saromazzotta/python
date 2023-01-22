from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)


@app.route('/ninja/add', methods=['POST'])
def add_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }

    dojo_id = request.form['dojo_id']
    Ninja.save(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninja/edit/<int:ninja_id>')
def edit_page(ninja_id):
    data = {
        "id" : ninja_id
    }

    return render_template("edit.html", ninja=Ninja.get_one(data))



@app.route('/ninja/<int:dojo_id>/<int:ninja_id>/update', methods=['POST'])
def update_ninja(dojo_id, ninja_id):
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "id" : ninja_id
    }

    Ninja.update(data)
    return redirect(f'/dojos/{dojo_id}')






@app.route('/ninja/<int:dojo_id>/<int:ninja_id>/delete')
def delete_ninja(dojo_id, ninja_id):
    data = {
        "id": ninja_id
    }

    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}')

