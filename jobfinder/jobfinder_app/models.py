from django.db import models

# Create your models here.

class Annonces(models.Model):
    titre = models.CharField(max_length=200)
    adresse = models.CharField(max_length=300)
    salaire = models.CharField(max_length=300)
    contrat = models.CharField(max_length=300)
    date = models.DateField()
    short_description = models.CharField(max_length=300)
    long_description = models.CharField(max_length=300)

    class Meta:
        db_table = 'Annonces'

class Entreprises(models.Model):
    nom_entreprise = models.CharField(max_length=100)
    pageweb = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    taille = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)

    class Meta:
        db_table = 'Entreprises'
