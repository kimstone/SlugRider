from django.db import models

import bcrypt
import re

class UserManager(models.Manager):

    def authenticate_credentials(self, email, password):
        try:
            user = User.objects.get(email=email)
        except:
            return False
        return bcrypt.checkpw(password.encode(), user.password.encode())


    def validate_login_form(self, data):

        errors = {}

        if len(data['email_address']) < 1:
            errors['email_address'] = "Email Address cannot be empty."

        if len(data['password']) < 1:
            errors['password'] = "Password cannot be empty."

        return errors


    def create_new_user(self, data):
        hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email_address'],
            password=hashed_pw,
        )

    def validate_registration_form(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}

        if len(data['first_name']) < 3:
            errors['first_name'] = "First name must be at least 2 characters."

        if data['first_name'].isalpha():
            pass
        else:
            errors['first_name'] = "First name must be letters only."

        if len(data['last_name']) < 3:
            errors['last_name'] = "Last name must be at least 2 characters."

        if data['last_name'].isalpha():
            pass
        else:
            errors['last_name'] = "Last name must be letters only."

        if not EMAIL_REGEX.match(data['email_address']):
            errors['email'] = ("Invalid email address!")

        # CHECK FOR UNIQUE EMAIL
        email_check = User.objects.filter(email=data['email_address']).exists()
        if email_check:
            errors['email'] = "That email address has been taken, choose another."

        if len(data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."

        if data['password'] != data['pw_confirm']:
            errors['password'] = "Passwords do not match."

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=150, unique=True)
    slugline = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

