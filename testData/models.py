from django.db import models

# Create your models here.
   
class Person(models.Model):
  name = models.CharField(max_length = 20)
  project = models.CharField(max_length = 40)
  year = models.IntegerField()
