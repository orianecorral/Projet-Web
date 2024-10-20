from django.shortcuts import render,redirect
from django.apps import apps
from jobfinder_compte.models import Particuliers
from jobfinder_compte.models import Entreprises
from jobfinder_compte.models import Utilisateurs
from jobfinder_app.models import Annonces, Candidatures
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


    return render(request,'Liste_utilisateur.html',{
        'particulier':Particulier,
        'annonces':annonces,
        'entreprises':Entreprise,
        'utilisateurs':Utilisateur,
        'TabPar':particulierform,
        'TabEnt':entrepriseform,
        'TabAnn':annonceform,
        'TabUti':userform,
        'mails':Utilisateur
        }
    )

def liste_candidature(request, pk):
    annonces = Annonces.objects.get(id=pk)
    candidatures = Candidatures.objects.all()
    candidaturesform = CandidaturesForm(request.POST)
    if request.method =='POST':
        if 'sauvegarderCand' in request.POST:
            ul = request.POST.get('sauvegarderCand')
            if not ul:
                candidaturesform = CandidaturesForm(request.POST)
            else:
                jul = Candidatures.objects.get(id=ul)
                candidaturesform = CandidaturesForm(request.POST,instance=jul)
            candidaturesform.save()
            candidaturesform = CandidaturesForm()
        if 'editerCand' in request.POST:
            ide = request.POST.get('editerCand')
            jul = Candidatures.objects.get(id=ide)
            candidaturesform = CandidaturesForm(instance=jul)
        if 'supprimerCand' in request.POST:
            ide = request.POST.get('supprimerCand')    
            jul = Candidatures.objects.get(id=ide)
            jul.delete()
    return render(request, 'liste_candidature.html', {'candidatures':candidatures, 'annonces':annonces,'TabCand':candidaturesform,})


def form_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        cmdp = request.POST.get('cmdp')

        # Vérification de l'unicité des mdp
        if (cmdp != password):
            messages.info(request,'Mot de Passe Incorect')
            return redirect('/compte/user_form/')

        # Vérification que l'email est unique
        if Utilisateurs.objects.filter(email=email).exists():
            messages.info(request,'Un compte avec cet email existe déjà')
            return redirect('/compte/user_form/')

        # Hashage du mdp
        # hash_password = make_password(password)
        # Ajout du email et mdp a Utilisateurs
        utilisateur = Utilisateurs.objects.create_user(
            username=email,
            email=email,
            password = password,
            is_particulier = True,
        )

        utilisateur.save()

        # Ajout du reste a Particuliers
        particulier = Particuliers.objects.create(
            user = utilisateur,
            nom = nom,
            prenom = prenom,
            telephone = telephone
        )
        particulier.save()

        return redirect('Liste_utilisateur.html')

    return render(request,'form_user.html')

# Création de compte Entreprises

def form_entreprise(request):
    if request.method == 'POST':
        nom_entreprise = request.POST.get('nom_entreprise')
        pageweb = request.POST.get('pageweb')
        adresse = request.POST.get('adresse')
        taille = request.POST.get('taille')
        description = request.POST.get('description')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cmdp = request.POST.get('cmdp')

        # Vérification de l'unicité des mdp
        if (cmdp != password):
            messages.info(request,'Mot de Passe Incorect')
            return redirect('/compte/entreprise_form/')

        if Utilisateurs.objects.filter(email=email).exists():
            messages.info(request,'Un compte avec cet email existe déjà')
            return redirect('/compte/entreprise_form/')

        utilisateur = Utilisateurs.objects.create_user(
            username=email,
            email=email,
            password = password,
            is_entreprise = True,
        )
        utilisateur.save()

        # Ajout du reste a Entreprise

        entreprise = Entreprises.objects.create(
            user = utilisateur,
            nom_entreprise = nom_entreprise,
            pageweb = pageweb,
            adresse = adresse,
            taille=taille,
            description=description,
        )
        entreprise.save()


        return redirect('Liste_utilisateur.html')
    # Apres il faudra redirect to user_page
    return render(request,'form_entreprise.html')

def form_annonce(request, pk):
    user = Utilisateurs.objects.get(id=pk)
    if request.method == 'POST':
        titre = request.POST.get('titre')
        adresse = request.POST.get('adresse')
        nom_entreprise = request.POST.get('nom_entreprise')
        salaire = request.POST.get('salaire')
        contrat = request.POST.get('contrat')
        date = request.POST.get('date')
        short_description = request.POST.get('short_description')
        long_description = request.POST.get('long_description')




        # Create a new patient entry in the database using the Patient model
        annonce = Annonces(
            titre=titre, 
            adresse=adresse, 
            nom_entreprise=nom_entreprise, 
            salaire=salaire, 
            contrat=contrat, 
            date=date, 
            short_description=short_description, 
            long_description=long_description, 
            entreprise_id=user.id
            )
        annonce.save()

        return redirect('Liste_utilisateur.html')
    
    return render(request, 'form_annonce.html')