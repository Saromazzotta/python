from app import app
from app.models.user import User
from flask import render_template, redirect, request, session




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
    User.save(request.form)
    return redirect("/dashboard")

@app.route('/dashboard', methods=['POST'])
def dashboard():
    return render_template("dashboard.html")


