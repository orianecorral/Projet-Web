# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Annonces, Candidatures
from jobfinder_compte.models import Particuliers, Utilisateurs, Entreprises
from django.contrib.auth import logout
from .models import Annonces, Candidatures
from jobfinder_compte.models import Particuliers, Utilisateurs, Entreprises
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib import messages


def home_page(request):
    particuliers = Particuliers.objects.all()
    entreprises = Entreprises.objects.all()
    particuliers = Particuliers.objects.all()
    entreprises = Entreprises.objects.all()
    if request.method == "POST":
        recherche = request.POST['recherche']
        lieu = request.POST['lieu']

        annonces = Annonces.objects.filter(
            Q(titre__contains=recherche) | 
            Q(nom_entreprise__contains=recherche) | 
            Q(contrat__contains=recherche)| 
            Q(short_description__contains=recherche)| 
            Q(long_description__contains=recherche)
            )
        if lieu:
            annonces = annonces.filter(Q(adresse__icontains=lieu))
        

        return render(request,'home_page.html',{'annonces':annonces, 'particuliers':particuliers, 'entreprises':entreprises})
    
    return render(request,'home_page.html', {'particuliers':particuliers, 'entreprises':entreprises})


def connexion_page(request):
    return render(request,'connexion.html')

def inscription_page(request):
    return render(request,'inscription.html')


def annonce_entry(request, pk):
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
        messages.success(request, "Votre annonce à bien été créée !")
        return redirect('jobfinder_compte:entreprise_page')
    
    return render(request, 'annonce_form.html')
    
# Candidature sans compte
def no_compte_candidature_entry(request, pk):
    annonces = Annonces.objects.get(id=pk)
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        
        # Create a new patient entry in the database using the Patient model
        candidatures = Candidatures(
            prenom=prenom, 
            nom=nom, 
            email=email, 
            telephone=telephone,
            annonce_id=annonces.id)
        candidatures.save()
        messages.success(request, "Votre candidature à bien été prise en compte !")
        return redirect('http://127.0.0.1:8000/jobfinder')
    
    return render(request, 'no_compte_candidature_form.html',{'annonces':annonces})


def compte_candidature_entry(request,pk,pz):
    annonces = Annonces.objects.get(id=pk)
    user = Utilisateurs.objects.get(id=pz)
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        
        # Create a new patient entry in the database using the Patient model
        candidatures = Candidatures(
            prenom=prenom, 
            nom=nom, 
            email=email, 
            telephone=telephone, 
            annonce_id=annonces.id,
            user_id=user.id)
        candidatures.save()

        messages.success(request, "Votre candidature à bien été pris en compte !")
        return redirect('http://127.0.0.1:8000/jobfinder')
    
    particuliers = Particuliers.objects.all()
    return render(request, 'compte_candidature_form.html', {'particuliers':particuliers, 'annonces':annonces})



def logout_user(request):
    logout(request)
    return redirect("home_page")

def logout_entreprise(request):
    logout(request)
    return redirect("home_page")
