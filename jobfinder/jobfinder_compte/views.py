from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Utilisateur
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, is_password_usable

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


# Pour le Logout

# def logout_user(request):
#     logout(request)
#     return redirect("jobfinder_app:home_page")
# def user_form(request):
#     return render(request,'user_form.html')
def user_form(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        username = request.POST.get('username')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        cmdp = request.POST.get('cmdp')
        if(cmdp == password):
            password =make_password(password)
            patient = Utilisateur(prenom=prenom, nom=nom, username=username, telephone=telephone, password=password)
            patient.save()
            return HttpResponse("Data successfully inserted!")
        elif(cmdp != password):
            messages.info(request,'Mot de Passe Incorect')
            return redirect('/compte/user_form/')
    return render(request,'user_form.html')