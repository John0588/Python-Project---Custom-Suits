from django.db import models

class user(models.Model):
 firstName = models.CharField(max_length=100)
 lastName = models.CharField(max_length=100)
 email = models.CharField(max_length=100)
 password = models.CharField(max_length=100)
 def __str__(self):
     return self.firstName + " " + self.lastName
