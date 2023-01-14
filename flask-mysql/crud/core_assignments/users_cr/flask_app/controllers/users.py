from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/read')
def read_all():
    users = User.get_all()
    return render_template("read.html", users=users)


@app.route('/user/new')
def form():
    return render_template("create.html")


@app.route('/user/new/process', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    user_id=User.save(data)
    return redirect(f'/user/show/{user_id}')


@app.route('/user/show/<int:user_id>')
def user_show(user_id):
    data = {
        "id": user_id
    }
    return render_template("users_show.html", user=User.get_one(data))


@app.route('/user/<int:user_id>/edit')
def user_edit(user_id):
    data = {
        "id": user_id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route('/user/<int:user_id>/update', methods=['POST'])
def user_update(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect(f'/user/show/{user_id}')


@app.route('/user/<int:user_id>/delete')
def user_delete(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect('/read')

