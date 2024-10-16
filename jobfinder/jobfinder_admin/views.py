from django.shortcuts import render
from django.apps import apps
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_app.models import Annonces
# Create your views here.
def tab_Particulier(request):
    Particulier =Particuliers.objects.all()
    return render(request,'Liste_utilisateur.html',{'particulier':Particulier})

def tab_entreprise(request):
    Entreprise =Entreprises.objects.all()
    return render(request,'Liste_utilisateur.html',{'entreprises':Entreprise})
def tab_annonce(request):
    annonces =Annonces.objects.all()
    return render(request,'Liste_utilisateur.html',{'annonces':annonces})