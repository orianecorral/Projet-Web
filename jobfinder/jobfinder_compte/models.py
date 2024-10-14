from django.db import models

# Create your models here.

class Utilisateurs(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telephone = models.CharField(max_length=300)
    mdp = models.TextField()

    class Meta:
        db_table = 'Utilisateurs'


class Entreprises(models.Model):

    SIZE_CHOICES = [
        ('0-10', '0-10'),
        ('10-250', '10-250'),
        ('250-5000', '250-5000'),
        ('+5000', '+5000'),
    ]

    nom_entreprise = models.CharField(max_length=200)
    pageweb = models.CharField(max_length=500)
    adresse = models.CharField(max_length=300)
    taille = models.CharField(max_length=100, choices=SIZE_CHOICES)
    description = models.TextField()
    email = models.CharField(max_length=200)
    password = models.TextField()

    class Meta:
        db_table = 'Entreprises'
