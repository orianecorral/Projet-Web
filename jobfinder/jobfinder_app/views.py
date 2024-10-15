# Create your views here.
from django.shortcuts import render,redirect
# from .forms import AnnoncesForm
from django.http import HttpResponse
from .models import Annonces
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    return render(request,'home_page.html')

def recherche_page(request):
    if request.method == "POST":
        recherche = request.POST['recherche']
        annonces = Annonces.objects.filter(Q(titre__contains=recherche) | Q(nom_entreprise__contains=recherche) | Q(contrat__contains=recherche)| Q(short_description__contains=recherche)| Q(long_description__contains=recherche))
        return render(request,'recherche_page.html',{'annonces':annonces})
    else:
        annonces = Annonces.objects.all()
        return render(request,'recherche_page.html',{'annonces':annonces})

def connexion_page(request):
    return render(request,'connexion.html')

def inscription_page(request):
    return render(request,'inscription.html')


def annonce_entry(request):
    return render(request, 'annonce_form.html')

def process_annonce_entry(request):
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
        patient = Annonces(titre=titre, adresse=adresse, nom_entreprise=nom_entreprise, salaire=salaire, contrat=contrat, date=date, short_description=short_description, long_description=long_description)
        patient.save()



        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")




def candidature_entry(request):
    return render(request, 'candidature_form.html')


# def create_annonce(request):
#     if request.method == "POST":
#         form = AnnoncesForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('search/')
#             except:
#                 pass
#     else:
#         form = AnnoncesForm()
#     return render(request, 'create.html', {'form':form})

# def retrieve_jobfinder(request):
#     annonces = Annonces.objects.all()
#     return render(request,'search.html',{'annonces':annonces})

def logout_user(request):
    logout(request)
    return redirect("home_page")

def logout_entreprise(request):
    logout(request)
    return redirect("home_page")
