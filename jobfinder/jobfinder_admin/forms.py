# myapp/forms.py 
from django import forms 
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_compte.models import Utilisateurs
from jobfinder_app.models import Annonces,Candidatures
from .forms import *


class particulierForm(forms.ModelForm):
    class Meta:
        model = Particuliers
        exclude = ["user_id","id"]
        fields = ["nom","prenom","telephone"]
 
class EntreprisesForm(forms.ModelForm):
    class Meta:
        model = Entreprises
        exclude = ["user_id","id"]
        fields = ["nom_entreprise","pageweb","adresse","taille","description"]
 
class AnnoncesForm(forms.ModelForm):
    class Meta:
        model = Annonces
        exclude = ["entreprise","id"]
 
class UtilisateursForm(forms.ModelForm):
    class Meta:
        model = Utilisateurs
        fields = ["email"]
        exclude = ["password","last_login","is_superuser","first_name","last_name","is_staff","is_active","date_joined","is_particulier","is_entreprise"]

class CandidaturesForm(forms.ModelForm):
    class Meta:
        model = Candidatures
        fields = ["prenom","nom","email", "telephone"]
        exclude = ["user","id","annonces"]