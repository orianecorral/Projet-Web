from django.shortcuts import render
from django.apps import apps
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_app.models import Annonces
from .forms import *
from django.contrib.auth import authenticate
# Create your views here.
def tab_Particulier(request):
    particulierform = particulierForm()
    entrepriseform = EntreprisesForm(request.POST)
    annonceform =AnnoncesForm(request.POST)
    userform = UtilisateursForm(request.POST)
    Particulier =Particuliers.objects.all()
    Entreprise =Entreprises.objects.all()
    annonces =Annonces.objects.all()
    if request.method =='POST': 
        if 'sauvegarderPar' in request.POST:
            ul = request.POST.get('sauvegarderPar')
            if not ul:
                particulierform = particulierForm(request.POST)
            else:
                jul = Particuliers.objects.get(id=ul)
                particulierform = particulierForm(request.POST,instance=jul)
            particulierform.save()
            particulierform = particulierForm()


        if 'sauvegarderEnt' in request.POST:
            ul = request.POST.get('sauvegarderEnt')
            if not ul:
                entrepriseform = EntreprisesForm(request.POST)
            else:
                jul = Entreprises.objects.get(id=ul)
                entrepriseform = EntreprisesForm(request.POST,instance=jul)
            entrepriseform.save()
            entrepriseform = EntreprisesForm()


        if 'sauvegarderAnn' in request.POST:
            ul = request.POST.get('sauvegarderAnn')
            if not ul:
                annonceform = AnnoncesForm(request.POST)
            else:
                jul = Annonces.objects.get(id=ul)
                annonceform = AnnoncesForm(request.POST,instance=jul)
            annonceform.save()
            annonceform = AnnoncesForm()
        if 'editerPar' in request.POST:
            ide = request.POST.get('editerPar')
            jul = Particuliers.objects.get(id=ide)
            particulierform = particulierForm(instance=jul)
        if 'editerAnn' in request.POST:
            ide = request.POST.get('editerAnn')
            jul = Annonces.objects.get(id=ide)
            annonceform = AnnoncesForm(instance=jul)
        if 'editerEnt' in request.POST:
            ide = request.POST.get('editerEnt')
            jul = Entreprises.objects.get(id=ide)
            entrepriseform = EntreprisesForm(instance=jul)
        if 'supprimerPar' in request.POST:
            ide = request.POST.get('supprimerPar')    
            jul = Particuliers.objects.get(id=ide)  #ici le problème est que je met particulier même si c'est entreprises ou annonces .
            jul.delete()
        if 'supprimerAnn' in request.POST:
            ide = request.POST.get('supprimerAnn')    
            jul = Annonces.objects.get(id=ide)  #ici le problème est que je met particulier même si c'est entreprises ou annonces .
            jul.delete()
        if 'supprimerEnt' in request.POST:
            ide = request.POST.get('supprimerEnt')    
            jul = Entreprises.objects.get(id=ide)  #ici le problème est que je met particulier même si c'est entreprises ou annonces .
            jul.delete()
    return render(request,'Liste_utilisateur.html',{'particulier':Particulier,'annonces':annonces,'entreprises':Entreprise,'TabPar':particulierform,'TabEnt':entrepriseform,'TabAnn':annonceform,'TabUti':userform})

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