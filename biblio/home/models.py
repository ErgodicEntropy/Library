from django.db import models

# Create your models here.


class Home(models.Model): #Django ORM: class -> table
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)


