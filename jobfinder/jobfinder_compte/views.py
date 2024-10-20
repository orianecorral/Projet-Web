from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Utilisateurs, Entreprises, Particuliers
from jobfinder_app.models import Annonces, Candidatures
from django.contrib import messages

from .forms import ParticuliersForm, UtilisateursForm, EntreprisesForm, AnnoncesForm

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

        messages.success(request, "Création d'un compte particulier réussie !")
        return redirect('http://127.0.0.1:8000/jobfinder')

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

        messages.success(request, "Création d'un compte entreprise réussie !")
        return redirect('http://127.0.0.1:8000/jobfinder')
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

        if user is not None and user.is_active:
            login(request, user)
            return redirect("jobfinder_compte:user_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")

    return render(request, 'connexion_user.html')

# Connection au compte Entreprises

def connexion_entreprise(request):
    if request.method =="POST":
        username = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("jobfinder_compte:entreprise_page")
        else:
            messages.info(request, "Identifiant ou mot de passe incorect")

    return render(request, 'connexion_entreprise.html')



# Fin de connection

# Affichage des pages Utilisateurs


def user_page(request):
    particuliers = Particuliers.objects.all()
    candidatures = Candidatures.objects.all()
    annonces = Annonces.objects.all()
    return render(request,'user_page.html',{'particuliers':particuliers, 'candidatures':candidatures, 'annonces':annonces})

def entreprise_page(request):
    entreprises = Entreprises.objects.all()
    annonces = Annonces.objects.all()
    candidatures = Candidatures.objects.all()
    return render(request,'entreprise_page.html',{'entreprises':entreprises,'annonces':annonces,'candidatures':candidatures})

def update_user_bis(request,pk):
    particulier = Particuliers.objects.get(user_id=pk)
    utilisateur = Utilisateurs.objects.get(id=pk)
    form1 = ParticuliersForm(instance = particulier)
    form2 = UtilisateursForm(instance = utilisateur)
    if request.method == 'POST':
        form1 = ParticuliersForm(request.POST, instance=particulier)
        form1.save()
        form2 = UtilisateursForm(request.POST, instance=utilisateur)
        form2.save()
        return redirect('/compte/user_page')

    context = {
        'particulier': particulier,
        'utilisateur' : utilisateur,
        'form1': form1,
        'form2': form2,
    }
    return render(request,'update_user.html',context)

def update_entreprise(request,pk):
    entreprise = Entreprises.objects.get(user_id=pk)
    utilisateur = Utilisateurs.objects.get(id=pk)
    form1 = EntreprisesForm(instance = entreprise)
    form2 = UtilisateursForm(instance = utilisateur)
    if request.method == 'POST':
        form1 = EntreprisesForm(request.POST, instance=entreprise)
        form1.save()
        form2 = UtilisateursForm(request.POST, instance=utilisateur)
        form2.save()
        return redirect('/compte/entreprise_page')

    context = {
        'entreprise': entreprise,
        'utilisateur' : utilisateur,
        'form1': form1,
        'form2': form2,
    }
    return render(request,'update_entreprise.html',context)


def update_annonce(request,pk):
    # entreprise = Entreprises.objects.get(user_id=pk)
    annonce = Annonces.objects.get(id=pk)
    # form1 = EntreprisesForm(instance = entreprise)
    form2 = AnnoncesForm(instance = annonce)
    if request.method == 'POST':
        # form1 = EntreprisesForm(request.POST, instance=entreprise)
        # form1.save()
        form2 = AnnoncesForm(request.POST, instance=annonce)
        form2.save()
        return redirect('/compte/entreprise_page')

    context = {
        # 'entreprise': entreprise,
        'annonce' : annonce,
        # 'form1': form1,
        'form2': form2,
    }
    return render(request,'update_annonce.html',context)

# Delete

def delete_particulier(request, pk):
    utilisateur = Utilisateurs.objects.get(id=pk)
    particulier = Particuliers.objects.get(user_id = pk)

    if request.method == 'POST':
        utilisateur.delete()
        particulier.delete()
        return redirect('http://127.0.0.1:8000/jobfinder')

    context = {
        'utilisateur': utilisateur,
        'particulier': particulier,
    }
    return render(request, 'remove-particulier.html', context)

def delete_entreprise(request, pk):
    utilisateur = Utilisateurs.objects.get(id=pk)
    entreprise =  Entreprises.objects.get(user_id = pk)

    if request.method == 'POST':
        utilisateur.delete()
        entreprise.delete()
        return redirect('http://127.0.0.1:8000/jobfinder')

    context = {
        'utilisateur': utilisateur,
        'entreprise': entreprise,
    }
    return render(request, 'remove-entreprise.html', context)

def delete_annonce(request, pk):
    # entreprise = Entreprises.objects.get(user_id=pk)
    annonce =  Annonces.objects.get(id = pk)

    if request.method == 'POST':
        annonce.delete()
        # entreprise.delete()
        return redirect('http://127.0.0.1:8000/compte/entreprise_page')

    context = {
        'annonce': annonce,
        # 'entreprise': entreprise,
    }
    return render(request, 'remove-annonce.html', context)
