from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Utilisateurs, Entreprises, Particuliers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, is_password_usable

# Create your views here.

# Création de profil

# Création de profil Particuliers:

def user_form(request):
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

        return HttpResponse("Data successfully inserted!")

    return render(request,'user_form.html')

# Création de compte Entreprises

def entreprise_form(request):
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
            
        if Utilisateurs.objects.filter(email=email).exist():
            messages.info(request,'Un compte avec cet email existe déjà')
            return redirect('/compte/user_form/')
        
        utilisateur = Utilisateurs.objects.create_user(
            username=email,
            email=email,
            password = password,
            is_entreprise = True,
        )
        utilisateur.save()

        # Ajout du reste a Particuliers

        entreprise = Entreprises.objects.create(
            user = entreprise,
            nom_entreprise = nom_entreprise,
            pageweb = pageweb,
            adresse = adresse,
            taille=taille,
            description=description,
        )
        entreprise.save()
 


        return HttpResponse("Data successfully inserted!")
    # Apres il faudra redirect to user_page
    return render(request,'entreprise_form.html')

# Fin de création

# Connection au compte

# Compte Particuliers

def connexion_user(request):
    if request.method =="POST":
        username = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("/user_page.html")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")
            
    return render(request, 'connexion_user.html')
    #     verif_user = Utilisateurs.objects.filter(email=email, password=password).exists()
    #     print(verif_user)
    #     if verif_user is True:
    #         # login(request, verif_user)
    #         return redirect("http://127.0.0.1:8000/jobfinder/")
    #     else:
    #         messages.info(request, "Identifiant ou mot de passe incorect")
    
    # return render(request, 'connexion_user.html')

# Connection au compte Entreprises

def connexion_entreprise(request):
    if request.method =="POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect("user_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")
    

# def connexion_user(request):
#     return render(request,'connexion_user.html')


# Fin de connection

# Affichage des pages Utilisateurs


def user_page(request):
    return render(request,'user_page.html')

def entreprise_page(request):
    return render(request,'entreprise_page.html')


# Pour le Logout

# def logout_user(request):
#     logout(request)
#     return redirect("jobfinder_app:home_page")