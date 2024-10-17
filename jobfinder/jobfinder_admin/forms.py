# myapp/forms.py 
from django import forms 
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_app.models import Annonces
from .forms import *

class particulierForm(forms.ModelForm):
    class Meta:
        model = Particuliers
        fields = '__all__'