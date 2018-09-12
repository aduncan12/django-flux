from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100, default="Name")
    email = models.CharField(max_length=100, default="Email")
    password = models.CharField(max_length=100, default="Password")

class Heritage(models.Model):
    name = models.CharField(max_length=100, default="Restaurant")
    address = models.CharField(max_length=100, default="San Francisco")
    yearOpened = models.CharField(max_length=10, null=True, default="1849")
    lat = models.FloatField(null=True, default=37.7749)
    lon = models.FloatField(null=True, default=-122.419)
    website = models.URLField(default="https://sfgov.org/")

class Legacy(models.Model):
    name = models.CharField(max_length=100, default="Restaurant")
    address = models.CharField(max_length=100, default="San Francisco")
    yearOpened = models.CharField(max_length=10, null=True, default="1849")
    lat = models.FloatField(null=True, default=37.7749)
    lon = models.FloatField(null=True, default=-122.4194)
    website = models.URLField(default="https://sfgov.org/")

    def __str__(self):
        return self.name
