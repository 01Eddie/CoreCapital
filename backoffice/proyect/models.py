from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Survey(models.Model):
    title = models.CharField(max_length=50)
