from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

def __str__(self):
    return self.first_name + self.last_name
