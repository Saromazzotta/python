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
        self.password = data['confirm_password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if len(user['password']) != len(user['confirm_password']):
            flash("Passwords must match.")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO users (first_name, last_name, email, password, confirm_password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s)
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
            email = %(emails)s;
        """

        result = connectToMySQL('users').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])
