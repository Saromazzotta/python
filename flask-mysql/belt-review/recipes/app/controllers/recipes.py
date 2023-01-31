from app import app
from flask import render_template, redirect, request, session, flash
from app.models.recipe import Recipe
from app.models import user


@app.route('/recipes')
def dashboard():

    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }

    return render_template("show_recipes.html", recipes=Recipe.get_all(), user=user.User.get_user_by_id(data))

@app.route('/recipes/<int:id>')
def recipe_card(id):

    user_data = {
        "id": id
    }

    user_id = {
        "id": session['user_id']
    }

    # data = {
    #     'id': recipe_id
    # }
    return render_template("recipe_card.html", recipe=Recipe.get_recipe_with_user(user_data), user=user.User.get_user_by_id(user_id))

@app.route('/recipes/new')
def add_recipe():
    return render_template("add_recipe.html")

@app.route('/recipes/add', methods=['POST'])
def post_recipe():

    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    

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

# @app.route('/recipes/delete')
# def recipe_delete():
