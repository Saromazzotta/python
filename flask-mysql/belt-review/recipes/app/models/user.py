from app import app
from app.config.mysqlconnection import connectToMySQL
from app.models import recipe
from flask import flash
import re
from flask_bcrypt import Bcrypt
# we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'recipes'
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # self.recipes = []

    @staticmethod
    def validate_registration(user):
        is_valid = True  # we assume this is true

        if User.get_by_email(user['email']):
            flash("Email already taken", "register")
            is_valid = False

        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Passwords must match.", "register")
            is_valid = False

        if len(user['first_name']) == 0:
            flash("Enter a first name", "register")
            is_valid = False

        if len(user['last_name']) == 0:
            flash("Enter a last name", "register")
            is_valid = False

        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email/password!", "login")
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
        """

        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """

        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT 
            *
        FROM 
            users
        WHERE 
            email = %(email)s
        """

        result = connectToMySQL(db).query_db(query, data)

        return cls(result[0]) if result else None

    @classmethod
    def get_user_by_id(cls, data):
        query = """
        SELECT 
            *
        FROM 
            users 

        WHERE 
            id = %(id)s;
        """

        results = connectToMySQL(db).query_db(query, data)

        return cls(results[0]) if results else None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL(db).query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users
    
#reversed this method in the recipe class instead

    # @classmethod
    # def get_user_with_recipes(cls,data):
    #     query = """
    #     SELECT 
	#         *
    #     FROM
	#         users
    #     LEFT JOIN
	#         recipes 
    #     ON
	#         recipes.user_id = users.id
    #     WHERE
    #         users.id = %(id)s
    #     """
    #     results = connectToMySQL('recipes').query_db(query,data)
    #     user = cls(results[0]) if results else None
    #     for row_from_db in results:
    #         recipe_data = {
    #             "id": row_from_db['recipes.id'],
    #             "name": row_from_db['name'],
    #             "description": row_from_db['description'],
    #             "instructions": row_from_db['instructions'],
    #             "date_made": row_from_db['date_made'],
    #             "under_30": row_from_db['under_30'],
    #             "created_at": row_from_db['recipes.created_at'],
    #             "updated_at": row_from_db['recipes.updated_at'],
    #             "user_id": row_from_db['user_id']
    #         }
    #         user.recipes.append(recipe.Recipe(recipe_data))
    #     return user