from django.db import models

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=200)

class Contact(models.Model):
  name  = models.CharField(max_length=200)
  age   = models.IntegerField(default=0) 
  emial = models.EmailField()

class Tag(models.Model):
  contact = models.ForeignKey(Contact)
  name    = models.CharField(max_length=50)