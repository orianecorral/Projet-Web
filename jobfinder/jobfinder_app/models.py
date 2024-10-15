from django.db import models
# from jobfinder_compte.models import Utilisateurs, Entreprises, Particuliers


# Create your models here.

class Annonces(models.Model):

    CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD 6 mois', 'CDD 6 mois'),
        ('CDD 12 mois', 'CDD 12 mois'),
        ('CDD 18 mois', 'CDD 18 mois'),
        ('Stage', 'Stage'),
        ('Stage 6 mois', 'Stage 6 mois'),
        ('Alternance', 'Alternance'),
    ]

    titre = models.CharField(max_length=400)
    adresse = models.CharField(max_length=500)
    nom_entreprise = models.CharField(max_length=300)
    salaire = models.CharField(max_length=300)
    contrat = models.CharField(max_length=300, choices=CONTRAT_CHOICES)
    date = models.DateField()
    short_description = models.CharField(max_length=150)
    long_description = models.TextField()
    # company_id = models.ForeignKey(Entreprises, on_delete=models.CASCADE, default=None)


    class Meta:
        db_table = 'Annonces'


class Candidatures(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'Candidatures'