from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    code = models.DecimalField()
    
    
    def __str__(self):
        return self.name





    