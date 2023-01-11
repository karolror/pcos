from django.db import models


# Test model
class Profile(models.Model):

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    age = models.CharField(max_length=2)
    bmi = models.CharField(max_length=2)
