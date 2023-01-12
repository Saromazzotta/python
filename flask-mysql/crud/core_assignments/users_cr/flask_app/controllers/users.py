from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/read')
def read_all():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)


@app.route('/user/new')
def form():
    return render_template("create.html")


@app.route('/user/new/process', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect('/read')


@app.route('/user/show/<int:user_id>')
def user_show(user_id):
    data = {
        "id": id
    }
    return render_template("users_show.html", user=User.get_one(data))
