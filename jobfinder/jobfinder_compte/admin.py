from django.contrib import admin
from .models import Utilisateurs, Entreprises

# Register your models here.
admin.site.register(Utilisateurs)
admin.site.register(Entreprises)