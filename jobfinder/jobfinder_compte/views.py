from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Utilisateur
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def connexion_entreprise(request):
    if request.method =="POST":
        email = request.POST["email"]
        mdp = request.POST["mdp"]

        user = authenticate(request, email = email, mdp = mdp)

        if user is not None:
            login(request, user)
            return redirect("user_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")
    


def connexion_user(request):
    if request.method =="POST":
        email = request.POST["email"]
        mdp = request.POST["mdp"]

        user = authenticate(request, email = email, mdp = mdp)

        if user is not None:
            login(request, user)
            return redirect("entreprise_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")



def entreprise_page(request):
    return render(request,'entreprise_page.html')


def user_page(request):
    return render(request,'user_page.html')


def entreprise_form(request):
    return render(request,'entreprise_form.html')

def user_form(request):
    return render(request,'user_form.html')


def process_user_form(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        mdp = request.POST.get('mdp')
        
        # Create a new patient entry in the database using the Patient model
        patient = Utilisateur(prenom=prenom, nom=nom, email=email, telephone=telephone, mdp=mdp)
        patient.save()



        return HttpResponse("Data successfully inserted!")
    # Apres il faudra redirect to user_page
    else:
        return HttpResponse("Invalid request method.")


# Pour le Logout

# def logout_user(request):
#     logout(request)
#     return redirect("jobfinder_app:home_page")