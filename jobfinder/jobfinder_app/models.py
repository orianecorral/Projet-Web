from django.db import models

# Create your models here.
from django.db import models

class Annonces(models.Model):
    annonce_id = models.CharField(max_length=30)
    titre = models.CharField(max_length=200)
    adresse = models.CharField(max_length=300)
    salaire = models.CharField(max_length=300)
    contrat = models.CharField(max_length=300)
    date = models.DateField()
    short_description = models.CharField(max_length=300)
    long_description = models.CharField(max_length=300)


    class Meta:
        db_table = 'Annonces'
