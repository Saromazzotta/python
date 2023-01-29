from app import app
from flask import render_template, redirect, request, session
from app.models.recipe import Recipe








@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/recipes/new')
def add_recipe():
    return render_template("add_recipe.html")

@app.route('/recipes/add', methods=['POST'])
def post_recipe():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made": request.form['date_made'],
        "under_30": request.form['under_30'],
        "user_id": session['user_id']
    }


    Recipe.save(data)

    return redirect('/recipes')
