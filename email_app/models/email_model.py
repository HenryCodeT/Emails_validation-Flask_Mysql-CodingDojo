from email_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


class Email:
    def __init__(self,data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_emails(cls):
        query = '''
                SELECT * FROM emails;
                '''
        response_query_emails = connectToMySQL('email_db').query_db(query)
        emails = []
        for email in response_query_emails:
            emails.append(cls(email))    
        return emails
    @classmethod
    def create_email(cls,data):
        query = '''
                INSERT INTO emails(email) VALUES (%(email)s)
                '''
        response_insert = connectToMySQL('email_db').query_db(query,data)
        return response_insert

    @classmethod
    def delete_email(cls,data):
        query = '''
                DELETE FROM emails WHERE id = %(id)s
                '''
        response_delete = connectToMySQL('email_db').query_db(query,data)

        return response_delete

    @staticmethod
    def validate_email(data):
        is_valid = True
        query = '''
                SELECT * FROM emails WHERE email = %(email)s
                '''
        response_get_email = connectToMySQL('email_db').query_db(query,data)
        if len(response_get_email)>=1:
            print("el mail ya existe")
            flash("el email ya existe")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            print("correo invalido")
            flash("correo invalido")
            is_valid = False

        return  is_valid 