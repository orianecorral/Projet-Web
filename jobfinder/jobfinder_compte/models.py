from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telephone = models.CharField(max_length=300)
    mdp = models.TextField()

    class Meta:
        db_table = 'Utilisateur'