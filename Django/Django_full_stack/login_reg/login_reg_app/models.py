from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['name']) < 3:
            errors['name'] = "Name is too short"
        users_with_name = User.objects.filter(name=requestPOST['name'])
        if len(users_with_name) > 0:
            errors['duplicate'] = "Name already taken"
        if len(requestPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Password and Password Confirmation must match"
        return errors

class User(models.Model):
    name = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
