# Create your views here.
from django.shortcuts import render, redirect
from .forms import AnnoncesForm
from .models import Annonces
from .forms import EntreprisesForm
from .models import Entreprises

# Fonctions pour Annonces
def create_jobfinder(request):
    if request.method == "POST":
        form = AnnoncesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = AnnoncesForm()
    return render(request, 'create.html', {'form':form})

def retrieve_jobfinder(request):
    annonces = Annonces.objects.all()
    return render(request,'search.html',{'annonces':annonces} )

def update_jobfinder(request,pk):
    annonces = Annonces.objects.get(id=pk)
    form = AnnoncesForm(instance=annonces)

    if request.method == 'POST':
        form = AnnoncesForm(request.POST, instance=annonces)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'annonces': annonces,
        'form': form,
    }
    return render(request,'update.html',context)


def delete_jobfinder(request, pk):
    annonces = Annonces.objects.get(id=pk)

    if request.method == 'POST':
        annonces.delete()
        return redirect('/search')

    context = {
        'annonces': annonces,
    }
    return render(request, 'remove.html', context)

# Fonction Entreprises

def create_entreprise(request):
    if request.method == "POST":
        form = EntreprisesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search-entreprise')
            except:
                pass
    else:
        form = EntreprisesForm()
    return render(request, 'create-entreprise.html', {'form':form})

def retrieve_entreprise(request):
    entreprises = Entreprises.objects.all()
    return render(request,'search-entreprise.html',{'entreprises':entreprises} )

def update_entreprise(request,pk):
    entreprises = Entreprises.objects.get(id=pk)
    form = EntreprisesForm(instance=entreprises)

    if request.method == 'POST':
        form = EntreprisesForm(request.POST, instance=entreprises)
        if form.is_valid():
            form.save()
            return redirect('/search-entreprise')

    context = {
        'entreprises': entreprises,
        'form': form,
    }
    return render(request,'update-entreprise.html',context)


def delete_entreprise(request, pk):
    entreprises = Entreprises.objects.get(id=pk)

    if request.method == 'POST':
        entreprises.delete()
        return redirect('/search-entreprise')

    context = {
        'entreprises': entreprises,
    }
    return render(request, 'remove-entreprise.html', context)
