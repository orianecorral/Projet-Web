from django import forms
from .models import Particuliers
from .models import Utilisateurs
from .models import Entreprises


class ParticuliersForm(forms.ModelForm):
    class Meta:
        model = Particuliers
        exclude = ["user_id","id"]
        fields = ["nom","prenom","telephone"]

class EntreprisesForm(forms.ModelForm):
        model = Entreprises
        exclude = ["user_id","id"]
        fields = ["nom_entreprise","pageweb","adresse","taille","description"]

class UtilisateursForm(forms.ModelForm):
    class Meta:
        model = Utilisateurs
        fields = ["email"]
        exclude = ["password","last_login","is_superuser","first_name","last_name","is_staff","is_active","date_joined","is_particulier","is_entreprise"]
