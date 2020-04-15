from django.db import models
import re

class OwnerManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST["name"]) < 4:
            errors["name"] = "Owner name must be 5 or more characters"
        name_regex = re.compile(r'^[a-zA-z ]+$')
        if not name_regex.match(requestPOST['name']):
            errors['invalid_name'] = "may only use letters in name"
        owners_with_name = Owner.objects.filter(name=requestPOST["name"])
        if len(owners_with_name) > 0:
            errors['same_name'] = "this name is already in use"
        if len(requestPOST["age"]) < 1:
            errors['age_missing'] = "age is required"
        if requestPOST["age"] != "" and int(requestPOST["age"]) < 0:
            errors["age"] = "age must be at least 0"
        return errors

class Owner(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OwnerManager()

class Chipmunk(models.Model):
    name = models.TextField()
    description = models.TextField()
    phone_number = models.TextField()
    owner = models.ForeignKey(Owner, related_name="chipmunks", on_delete=models.CASCADE)
    owners_that_voted = models.ManyToManyField(Owner, related_name="chipmunks_voted_for")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
