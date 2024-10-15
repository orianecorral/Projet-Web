from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Création de la base de donnée général qui contient les Particuliers et les Entreprises

class Utilisateurs(AbstractUser):
    is_particulier = models.BooleanField(default=False)
    is_entreprise = models.BooleanField(default=False)


    class Meta:
        db_table = 'Utilisateurs'
    # Element pas obligatoire représente un chaine de charactere permet de changer l'affichage de :
    # <Utilisateur: Utilisateur object (1)> => email
    def __str__(self):
        return self.email



# Création de la table Particuliers

class Particuliers(models.Model):
    # Lien en OnetoOne avec la table Utilisateurs avec l'option delete qui efface les données si ils sont
    # effacés de la table Utilisateur
    user = models.OneToOneField(Utilisateurs, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=300, null=True)
    telephone = models.CharField(max_length=300, null=True)

    class Meta:
        db_table = 'Particuliers'

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Entreprises(models.Model):

    SIZE_CHOICES = [
        ('0-10', '0-10'),
        ('10-250', '10-250'),
        ('250-5000', '250-5000'),
        ('+5000', '+5000'),
    ]
    user = models.OneToOneField(Utilisateurs, on_delete=models.CASCADE)
    nom_entreprise = models.CharField(max_length=200,null=True)
    pageweb = models.CharField(max_length=500, null=True)
    adresse = models.CharField(max_length=300, null=True)
    taille = models.CharField(max_length=100, choices=SIZE_CHOICES, null=True)
    description = models.TextField()


    class Meta:
        db_table = 'Entreprises'

    def __str__(self):
        return f"{self.nom_entreprise}"
