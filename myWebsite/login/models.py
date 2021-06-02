from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    #password = models.CharField(max_length=30)
    #fname = models.CharField(max_length=10)
    #lname = models.CharField(max_length=10)
    #age = models.IntegerField()

    def __str__(self):
        return f"Username is {self.username}"#, First Name is {self.fname}, Last Name is {self.lname}, And the Password is {self.password}"