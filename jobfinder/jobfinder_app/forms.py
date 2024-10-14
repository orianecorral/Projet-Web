from django import forms
from .models import Annonces
from .models import Entreprises

class AnnoncesForm(forms.ModelForm):
    class Meta:
        model = Annonces
        fields = "__all__"

class EntreprisesForm(forms.ModelForm):
    class Meta:
        model = Entreprises
        fields = "__all__"
