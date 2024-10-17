from django.shortcuts import render
from django.apps import apps
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_app.models import Annonces
from .forms import *
from django.contrib.auth import authenticate
# Create your views here.
def tab_Particulier(request):
    if request.method =='POST':
        if 'sauvegarder' in request.POST:
            print('bouton sauvegarde')
        if 'editer' in request.POST:
            print('bouton editer')
        if 'supprimer' in request.POST:
            print('bouton supprimer')
    particulierform = particulierForm()
    Particulier =Particuliers.objects.all()
    return render(request,'Liste_utilisateur.html',{'particulier':Particulier,'TabPar':particulierform},)

def tab_entreprise(request):
    Entreprise =Entreprises.objects.all()
    return render(request,'Liste_utilisateur.html',{'entreprises':Entreprise})
def tab_annonce(request):
    annonces =Annonces.objects.all()
    return render(request,'Liste_utilisateur.html',{'annonces':annonces})
def CoAdmin(request):
    print('testtttttttt')
    user = authenticate(is_superuser = 1)
    if user is not None:
        print('je suis co')
        return render(request,'Liste_utilisateur.html')
    else:
        print('jesuis pasco')
        return render(request,'Liste_utilisateur.html')
    
def suprimmer(request):
    print('placeholder')
def editer(request):
    print('placeholder update')
def sauvegarder(request):
    print('placeholder sauvegarde')