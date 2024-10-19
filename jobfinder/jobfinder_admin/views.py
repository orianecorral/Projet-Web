from django.shortcuts import render,redirect
from django.apps import apps
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_compte.models import Utilisateurs
from jobfinder_app.models import Annonces
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

# code de vérification des admins
def CoAdmin(request):
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/jobfinder/') #url qui renvoie pas directement au tab admin pour raison de sécurité
        else:
             messages.info(request, "Identifiant ou mot de passe incorect")
    return render(request,'connexion_admin.html')
    
def tab_Particulier(request):
    particulierform = particulierForm()
    entrepriseform = EntreprisesForm(request.POST)
    annonceform =AnnoncesForm(request.POST)
    userform = UtilisateursForm(request.POST)
    Particulier =Particuliers.objects.all()
    Utilisateur = Utilisateurs.objects.all()
    Entreprise =Entreprises.objects.all()
    annonces =Annonces.objects.all()
    if request.method =='POST': #par ent et ann correspondent chacun à la modif d'un tableau (particulier entreprise et annonce)
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
            jul = Particuliers.objects.get(id=ide)
            jul.delete()
        if 'supprimerAnn' in request.POST:
            ide = request.POST.get('supprimerAnn')    
            jul = Annonces.objects.get(id=ide)
            jul.delete()
        if 'supprimerEnt' in request.POST:
            ide = request.POST.get('supprimerEnt')    
            jul = Entreprises.objects.get(id=ide)
            jul.delete()
    return render(request,'Liste_utilisateur.html',{'particulier':Particulier,'annonces':annonces,'entreprises':Entreprise,'TabPar':particulierform,'TabEnt':entrepriseform,'TabAnn':annonceform,'TabUti':userform,'mails':Utilisateur})