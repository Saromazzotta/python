from app import app
from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true

        if User.get_by_email(user['email']):
            flash("Email already taken", "register")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False

        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Passwords must match.")
            is_valid = False
            
        if len(user['first_name']) == 0:
            flash("Enter a first name", "register")
            is_valid = False

        if len(user['last_name']) == 0:
            flash("Enter a last name", "register")
            is_valid = False



        return is_valid


    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        return connectToMySQL('users').query_db(query,data)
    

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

        result = connectToMySQL('users').query_db(query, data)

        return cls(result[0]) if result else None
