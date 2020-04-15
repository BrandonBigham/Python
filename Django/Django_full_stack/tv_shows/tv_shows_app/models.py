from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST["title"]) < 2:
            errors["title"] = "Title must be at least 2 characters"
        if len(requestPOST["network"]) < 3:
            errors['network'] = "Network name must be at least 3 characters"
        if len(requestPOST["description"]) < 10:
            errors["description"] = "description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.TextField()
    network = models.TextField()
    release_date = models.TextField()
    description = models.TextField()
    objects = ShowManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
