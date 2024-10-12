# Create your views here.
from django.shortcuts import render
# from .forms import AnnoncesForm
from django.http import HttpResponse
from .models import Annonces


def home_page(request):
    return render(request,'home_page.html')

def recherche_page(request):
    annonces = Annonces.objects.all()
    return render(request,'recherche_page.html',{'annonces':annonces})


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
