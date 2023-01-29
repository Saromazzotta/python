from app import app
from flask_bcrypt import Bcrypt
from app.models.user import User
from app.models.recipe import Recipe
from flask import render_template, redirect, request, session, flash

@app.route('/')
def index():
    return render_template("index.html")


bcrypt = Bcrypt(app)


@app.route('/register', methods=['POST'])
def register():

    if not User.validate_registration(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
    }

    user_id = User.save(data)

    session['user_id'] = user_id
    return redirect("/recipes")

@app.route('/recipes')
def dashboard():

    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }

    all_recipes = Recipe.get_all()
    return render_template("show_recipes.html", user=User.get_one(data), recipes=all_recipes)


@app.route('/login', methods=['POST'])
def login():

    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)

    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')

    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/recipes")


