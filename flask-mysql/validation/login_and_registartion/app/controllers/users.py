from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from app.models.user import User
from flask import render_template, redirect, request, session, flash


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    #if there are errors:
    #We call the staticmethod on model to validate
    if not User.validate_registration(request.form):
        #redirect to the route where the form is rendered.
        return redirect('/')
    #else no errors:

    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
        "confirm_password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/success")


@app.route('/success')
def dashboard():
    return render_template("success.html")


@app.route('/login', methods=['POST'])
def login():
    if not User.validate_user(request.form):
        return redirect('/')

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
    return redirect("/success")



@app.route('/logout')
def logout():
    return redirect("/")


