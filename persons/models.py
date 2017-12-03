from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    first_names = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=120, blank=True, null=True)
    birth_source_doc = models.CharField(max_length=120, blank=True, null=True)
    birth_certificate = models.TextField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    death_place = models.CharField(max_length=120, blank=True, null=True)
    death_source_doc = models.CharField(max_length=120, blank=True, null=True)
    death_certificate = models.TextField(blank=True, null=True)
    wedding_date = models.DateField(blank=True, null=True)
    wedding_place = models.CharField(max_length=120, blank=True, null=True)
    wedding_source_doc = models.CharField(max_length=120, blank=True, null=True)
    wedding_certificae = models.CharField(max_length=120, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
