from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=30)
    mdp = models.CharField(max_length=50)

class Person(models.Model):
    prenom = models.CharField(max_length=70)
    nom = models.CharField(max_length=70)
