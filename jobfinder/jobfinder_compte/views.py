from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Utilisateurs, Entreprises
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def connexion_entreprise(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("user_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")
    

# def connexion_user(request):
#     return render(request,'connexion_user.html')

def connexion_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate( username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home_page.html")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")
    
    return render(request, 'connexion_user.html')



def entreprise_page(request):
    return render(request,'entreprise_page.html')


def user_page(request):
    return render(request,'user_page.html')


def entreprise_form(request):
    if request.method == 'POST':
        nom_entreprise = request.POST.get('nom_entreprise')
        pageweb = request.POST.get('pageweb')
        adresse = request.POST.get('adresse')
        taille = request.POST.get('taille')
        description = request.POST.get('description')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new patient entry in the database using the Patient model
        patient = Entreprises(nom_entreprise=nom_entreprise, pageweb=pageweb, adresse=adresse, taille=taille, description=description, username=username, password=password)
        patient.save()



        return HttpResponse("Data successfully inserted!")
    # Apres il faudra redirect to user_page
    return render(request,'entreprise_form.html')



def user_form(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        username = request.POST.get('username')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        
        # Create a new patient entry in the database using the Patient model
        patient = Utilisateurs(prenom=prenom, nom=nom, username=username, telephone=telephone, password=password)
        patient.save()



        return HttpResponse("Data successfully inserted!")
    
    # Apres il faudra redirect to user_page
    return render(request,'user_form.html')


# Pour le Logout

# def logout_user(request):
#     logout(request)
#     return redirect("jobfinder_app:home_page")