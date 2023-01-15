from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data('id')
        self.name = data('name')
        self.created_at = data('created_at')
        self.updated_at = data('updated_at')

        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        """
        return connectToMySQL('ninjas').query_db(query,data)
    
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = """
        SELECT 
            *
        FROM
            dojos

        LEFT JOIN
            ninjas 
        ON
            ninjas.dojo_id = dojos.id
        WHERE
            dojos.id = %(id)s;
        """
        results = connectToMySQL('ninjas').query_db(query,data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['ninjas.first_name'],
                "last_name" : row_from_db['ninjas.last_name'],
                "age" : row_from_db['ninjas.age'],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo